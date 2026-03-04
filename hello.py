def main():
    from escpos.printer import Serial

    """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
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
    # p.text("Hello World\n")
    #
    p.image("sturmico.png")
    p.image("horse.png")
    p.text("\nNo. 8\n")
    p.text("David Hasselhoff\n")
    p.text("2000 Ω\n")

    p.cut()


if __name__ == "__main__":
    main()
