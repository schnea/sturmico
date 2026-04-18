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
p.set(align="center")


@app.get("/health")
def health():
    return {"message": "Hello World"}


@app.get("/print/{race_no}/{horse_no}/{horse}/{amount}")
def read_item(race_no:int, horse_no: int, horse: str, amount: int):
    """Seiko Epson Corp. Receipt Printer (EPSON TM-T88III)"""
    horse_img = "horse.png" if race_no <= 1 else "horsereverse.png"
    # p.text("Hello World\n")
    p.image("sturmico.png")
    p.image(horse_img)
    p.text(f"\nRennen {race_no} \n")
    p.text(f"\n#{horse_no} \n")
    p.text(f"{horse}\n")
    p.text(f"{amount} Ohm\n")

    p.cut()

    return {"item_id": horse_no}
