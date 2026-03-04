from escpos.printer import Serial
from fastapi import FastAPI

app = FastAPI()
p = Serial(
    devfile="/dev/ttyUSB0",
    baudrate=38400,
    bytesize=8,
    parity="N",
    stopbits=1,
    timeout=1.00,
    dsrdtr=True,
    profile="TM-T88III",
)


@app.get("/health")
def health():
    return {"message": "Hello World"}


@app.get("/print/{horse_no}/{horse}/{amount}")
def read_item(horse_no: int, horse: str, amount: int):
    """Seiko Epson Corp. Receipt Printer (EPSON TM-T88III)"""
    # p.text("Hello World\n")
    p.image("sturmico.png")
    p.image("horse.png")
    p.text(f"\n#{horse_no} \n")
    p.text(f"{horse}\n")
    p.text(f"{amount} Ohm\n")

    p.cut()

    return {"item_id": horse_no}
