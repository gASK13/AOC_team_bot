import os
import json
import urllib
import boto3
import datetime

USER_AGENT = os.environ['USER_AGENT']
RETRY_PROTECTION = 1  # minute
SNS_TOPIC = os.environ['SNS_TOPIC']

def load_current_data():
    request = urllib.request.Request("https://adventofcode.com/2023/leaderboard/private/view/16961.json")
    request.add_header('User-Agent', USER_AGENT)
    request.add_header('Cookie', f'session={os.environ["AOC_SESSION"]}')
    return json.loads(urllib.request.urlopen(request).read())


def format_message(day, member, new_data, day_part='1'):
    # get order of the star of the day
    order = 1
    when = new_data['members'][member]['completion_day_level'][day][day_part]['get_star_ts']
    for other in new_data['members']:
        if day in new_data['members'][other]['completion_day_level']:
            if day_part in new_data['members'][other]['completion_day_level'][day]:
                if new_data['members'][other]['completion_day_level'][day][day_part]['get_star_ts'] < when:
                    order += 1

    return {'time': new_data['members'][member]['completion_day_level'][day][day_part]['get_star_ts'],
            'message': f"{new_data['members'][member]['name']} vyřešil {'první' if day_part == '1' else 'druhou'} část dne {day} jako {order}. - dobrá práce!"}


def find_best(data):
    # find member in data with highest local_score
    if len(data['members']) == 0:
        return [], 0
    _max = max([data['members'][member]['local_score'] for member in data['members']])
    return sorted([data['members'][member]['name'] for member in data['members'] if data['members'][member]['local_score'] == _max]), _max


def site_notification(message):
    boto3.client('sns', region_name='us-east-1').publish(
        TopicArn=SNS_TOPIC,
        Message=message,
        Subject=f'Advent Of Code',
        MessageStructure='text'
    )


def lambda_handler(event, context):
    # AWS Resource and Client
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('aoc')

    # Get the data for current year (rollover in summer)
    year = int(datetime.datetime.now().year)
    if int(datetime.datetime.now().month) < 12:
        year -= 1

    # get item for year = 2023 from dynamodb
    dbresp = table.get_item(Key={'year': year})

    # I want to query the API, parse the JSON
    # then find for each user what changed since last time
    # and then print the changes to email thread
    if 'Item' in dbresp:
        if dbresp['Item']['last_check'] > (int(datetime.datetime.now().timestamp()) - 60 * RETRY_PROTECTION):

            print('Too soon! Wait a bit!')
            # less than one minute? give back
            return {
                'message': 'Too soon! Wait a bit!',
                'statusCode': 418  # aka I'm a teapot
            }

        old_data = json.loads(dbresp['Item']['data'])
        if 'members' not in old_data:
            old_data['members'] = {}
        new_data = load_current_data()

        new_info = []
        for member in new_data['members']:
            if member not in old_data['members']:
                new_info.append({'time': 0,
                                 'message': f"Do řeže se přidal nový bojovník. Vítej, {new_data['members'][member]['name']}!"})
                # any stars they gained are new stars!
                for day in new_data['members'][member]['completion_day_level']:
                    new_info.append(format_message(day, member, new_data))
                    if '2' in new_data['members'][member]['completion_day_level'][day]:
                        new_info.append(format_message(day, member, new_data, day_part='2'))
            else:
                if new_data['members'][member]['local_score'] > old_data['members'][member]['local_score']:
                    for day in new_data['members'][member]['completion_day_level']:
                        # compare part 1 and part 2
                        if day not in old_data['members'][member]['completion_day_level']:
                            new_info.append(format_message(day, member, new_data))
                        elif '2' in new_data['members'][member]['completion_day_level'][day] and '2' not in \
                                old_data['members'][member]['completion_day_level'][day]:
                            new_info.append(format_message(day, member, new_data, day_part='2'))

        # - leader change !!!
        old_best = find_best(old_data)
        new_best = find_best(new_data)
        if old_best != new_best:
            new_info.append({'time': 999999999999999,
                             'message': f"Nově vede {new_best[0]} s {new_best[1]} body!"})

        # sort new_info by time
        new_info = sorted(new_info, key=lambda x: x['time'])

        # print it first
        for info in new_info:
            print(info['message'])

        print(f'Saving check from now - {int(datetime.datetime.now().timestamp())}')
        table.put_item(
            Item={'year': year, 'data': json.dumps(new_data), 'last_check': int(datetime.datetime.now().timestamp())})
    else:
        return {
            'message': f'No data in DB for {year}!',
            'statusCode': 500
        }

    return {
        'message': 'OK',
        'statusCode': 200
    }


