import logging

import uvicorn

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


def run():
    uvicorn.run("currency_converter.app:app", reload=True)


if __name__ == "__main__":
    run()
