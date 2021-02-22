import requests
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

# endpoint = "https://api.mainnet-beta.solana.com"
endpoint = "https://solana-api.projectserum.com"

addresses = [
    "fArUAncZwVbMimiWv5cPUfFsapdLd8QMXZE4VXqFagR",
    "DmKR61BQk5zJTNCK9rrt8fM8HrDH6DSdE3Rt7sXKoAKb",
    "HoVhs7NAzcAaavr2tc2aaTynJ6kwhdfC2B2Z7EthKpeo",
    "85WdjCsxksAoCo6NNZSU4rocjUHsJwXrzpHJScg8oVNZ",
    "HuBBhoS81jyHTKMbhz8B3iYa8HSNShnRwXRzPzmFFuFr",
    "5unqG9sYX995czHCtHkkJvd2EaTE58jdvmjfz1nVvo5x",
    "Faszfxg7k2HWUT4CSGUn9MAVGUsPijvDQ3i2h7fi46M6",
    "G2zmxUhRGn12fuePJy9QsmJKem6XCRnmAEkf8G6xcRTj",
    "CvcqJtGdS9C1jKKFzgCi5p8qsnR5BZCohWvYMBJXcnJ8",
    "5fHS778vozoDDYzzJz2xYG39whTzGGW6bF71GVxRyMXi",
]


def get_ray_supply():
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenSupply",
        "params": ["4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R"],
    }

    response = requests.post(endpoint, json=data)

    return int(
        response.json()
        .get("result", {})
        .get("value", {})
        .get("amount", "555000000000000")
    )


def get_ray_balance(address):
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenAccountBalance",
        "params": [address],
    }

    response = requests.post(endpoint, json=data)

    return int(
        response.json().get("result", {}).get("value", {}).get("amount", "0")
    )


@app.get("/ray/totalcoins", response_class=PlainTextResponse)
def totalcoins():
    return str(get_ray_supply())


@app.get("/ray/circulating", response_class=PlainTextResponse)
def circulating():
    circulating = get_ray_supply()

    for address in addresses:
        balance = get_ray_balance(address)
        circulating -= balance

    return str(circulating / 1e6)
