import nfc
from binascii import hexlify


# 学籍番号のサービスコード
card_service_code = 0x1A8B

def on_connect(tag):
    idm, pmm = tag.polling(system_code=0xfe00)
    tag.idm, tag.pmm, tag.sys = idm, pmm, 0xfe00

    sc = nfc.tag.tt3.ServiceCode(card_service_code >> 6, card_service_code & 0x3f)
    bc = nfc.tag.tt3.BlockCode(0, service=0)
    data = tag.read_without_encryption([sc], [bc])
    print ('あなたの学生番号は' + data[4:11].decode() + 'です．')


def main():
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect': on_connect})


if __name__ == '__main__':
    main()
