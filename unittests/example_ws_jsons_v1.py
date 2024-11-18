api_record = {  # copied from swagger hub
    "providerId": "1234567890123",
    "apiId": "example",
    "majorVersion": 1,
    "url": "https://www.example.org/api/resource/v1",
    "additionalMetadata": None,
    "lastUpdated": "2024-10-01T00:00:00Z",  # changed this to Z because pydantic prefers 'Z' over '+00:00'
    "revision": 1,
    "status": "Test",
}

contact_info = {"email": "foo@bar.inv", "phone": "00491234567890"}  # handwritten

service_info = {  # handwritten
    "version": "v1.2.3",
    "contact": contact_info,
    "lastUpdated": "2024-11-16T00:00:00Z",
    "revision": 17,
}
