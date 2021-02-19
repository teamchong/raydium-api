import requests
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


def get_ray_supply():
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenSupply",
        "params": ["4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R"],
    }

    response = requests.post("https://api.mainnet-beta.solana.com", json=data)

    return (
        response.json()
        .get("result", {})
        .get("value", {})
        .get("uiAmount", "555000000.0")
    )


@app.get("/ray/totalcoins", response_class=PlainTextResponse)
def totalcoins():
    return str(get_ray_supply())


@app.get("/ray/circulating", response_class=PlainTextResponse)
def circulating():
    return str(get_ray_supply() * 0.07)
