def generate_solved_message(data):
    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.0",
                    "body": [
                        {
                            "type": "ColumnSet",
                            "id": "9c721267-5779-727d-02e5-2b16c01fa258",
                            "columns": [
                                {
                                    "type": "Column",
                                    "id": "24a8e464-4649-c89d-987e-409c927e0ebe",
                                    "padding": "None",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "Image",
                                            "id": "6d86683b-8671-317b-0785-175b5619a4b3",
                                            "url": f"{data['image']}",
                                            "altText": "",
                                            "size": "Large"
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "id": "50ea9f84-be5c-eba9-29e8-79e228f21fb4",
                                    "padding": "None",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "id": "9b935c5b-7e6d-8718-f70d-b7a111f461f4",
                                            "text": f"{data['username']} právě vyřešil data['day']. den, {'první' if data['part'] == 1 else 'druhou'} část!",
                                            "wrap": True,
                                            "weight": "Bolder"
                                        },
                                        {
                                            "type": "TextBlock",
                                            "id": "09408bf2-6a2a-6a36-4720-45e24efde4bf",
                                            "text": f"Podařilo se mu to jako {data['order']}., přesně v {data['when']}",
                                            "wrap": True
                                        },
                                        {
                                            "type": "TextBlock",
                                            "id": "075c5afe-930d-5434-d4a6-465c09287c7e",
                                            "text": f"{data['after']}Jeho nové skóre je teď {data['score']} a je na {data['place']}. místě.",
                                            "wrap": True
                                        },
                                        {
                                            "type": "ActionSet",
                                            "actions": [
                                                {
                                                    "type": "Action.OpenUrl",
                                                    "id": "57f63bc4-abc2-e436-a952-035454636c1a",
                                                    "title": "Ukázat tabulku",
                                                    "url": f"{data['url']}"
                                                },
                                                {
                                                    "type": "Action.OpenUrl",
                                                    "id": "fb9689cd-f451-b93c-dadd-7a8d429f4cac",
                                                    "title": f"Luštit den {data['day']}",
                                                    "url": f"https://adventofcode.com/{data['year']}/day/{data['day']}"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "padding": "None"
                        }
                    ],
                    "padding": "None"
                }
            }
        ]
    }
