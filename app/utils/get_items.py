import requests


async def get_items(query: str, typed: int = None) -> list[dict]:
    if not query and not typed:
        return []

    search_url = "https://vpic.nhtsa.dot.gov/api/vehicles/GetParts?format=json"

    if typed != "":
        search_url = (
            f"https://vpic.nhtsa.dot.gov/api/vehicles/GetParts?type={typed}&format=json"
        )

    items = requests.get(search_url).json()
    print(search_url)

    transformed_results = [
        {
            "Name": item["Name"],
            "ManufacturerName": item["ManufacturerName"],
            "ManufacturerId": item["ManufacturerId"],
            "URL": item["URL"],
        }
        for item in items["Results"]
        if query.lower() in item["Name"].lower()
    ]

    return transformed_results


async def get_manufacturer_data(manufacturerId: int) -> dict:
    search_url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmanufacturerdetails/{manufacturerId}?format=json"
    items = requests.get(search_url).json()
    transformed_results = [
        {
            "Address": item["Address"],
            "Address2": item["Address2"],
            "City": item["City"],
            "ContactEmail": item["ContactEmail"],
            "ContactFax": item["ContactFax"],
            "ContactPhone": item["ContactPhone"],
            "Country": item["Country"],
            "Type": ",".join(
                [type_item["Name"] for type_item in item["ManufacturerTypes"]]
            ),
        }
        for item in items["Results"]
    ]
    return transformed_results
