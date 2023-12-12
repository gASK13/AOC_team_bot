def generate_champion_message(data):
    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "contentUrl": null,
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
                                    "padding": "Default",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "Image",
                                            "id": "6d86683b-8671-317b-0785-175b5619a4b3",
                                            "url": "data:image/png;base64,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",
                                            "size": "Large"
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "id": "50ea9f84-be5c-eba9-29e8-79e228f21fb4",
                                    "padding": "Default",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "id": "9b935c5b-7e6d-8718-f70d-b7a111f461f4",
                                            "text": f"{data['leader']} se ujal vedení!",
                                            "wrap": True,
                                            "weight": "Bolder"
                                        },
                                        {
                                            "type": "TextBlock",
                                            "id": "09408bf2-6a2a-6a36-4720-45e24efde4bf",
                                            "text": f"Právě předběhl {data['second']} a s {data['leader_points']} body je na prvním místě.",
                                            "wrap": True
                                        },
                                        {
                                            "type": "TextBlock",
                                            "id": "075c5afe-930d-5434-d4a6-465c09287c7e",
                                            "text": f"{data['second']} má {data['second_points']} bodů.",
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
