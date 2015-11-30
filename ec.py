#-*- encoding: utf-8 -*-
import logging
import sys
import os
import Image, ImageFont, ImageDraw
from string import lower, upper
 
#logging.getLogger("code128").setLevel(logging.DEBUG)
#logging.getLogger("code128").addHandler(logging.StreamHandler(sys.stdout))
#12-80  10-80 10-60 12-60 10-70 12-70 10-70


# courbB08.pil PIL Font file uuencoded
courB08_pil ="""eJztl91rFkcUxp+Zt7vGFYzVtiJKICgYlLRWkaBBVGgDraFGCH5gsQp+QMBqabAVRYJYAlakCkoh
CpYgxaLkIu1NvLBeSAStglpqL6xQAsVe2AuL5u2buH3mzGaYPf9AKWTl8d3nl7MzZ2bnazvea9+9
7+PurFWut5e0Zu+s7VybYfKavP7LK3X/5TlM4Q3/OWbyf1ARD/6mgb2SjwtPhbpnq0iKZ6ahrmCj
wqbxdgamRnHOA69jimN5zvIS8cDcUEeVdYzRAw1FHcJYXgPvG4s6Jlgj7xeEequS3wLeNvGvnrEO
tq+Jt82szT+b86+WHlgS2jHGuHF6YHnog1zaupxqCcy3t4X3rVG9iXhgjW+bsFQ80BaxRDywTrF1
VId6toPaqOI2UlsV20ptV2w7tUuxXVSXYl3UvoIZ9kFFPPBJ6D/HLD3QXbwjyDjI6YHPiz5FXiN7
SQ8cDu/N9/1h3veEOP/Oe6gvQnmuvYYe+NL3qYyNVDxw2seF8XKa+jrKJREPnFdx56l+xfqpS4pd
ogZUeQPU91FcKh64GveBeOCaKu8adUM9e4O6reJuU/cUu0c9VM8+pB6r/B5TI+rZEerPUpyhB/6K
5lsqHniuyntO1VR5Nb5CU86FHqZOsTqqXrF66o2ojlQ8zDwVN4+aX86FHqYpXg9YLeevWRzPc7LF
ZG+V1wN6mKXxvMzH6GFaJua5zGNLD7MqmtNcc+hh1oT1oCb5cf6aNj92mbPMGXqY9jCPasLaqQ1h
jMv8pYfZpOI2UR9GcYl4mB1RnMtvB9me8N583B5qb3mNoIf5NGJc1+hhPvPrrjybioc5op49Qh0L
dfj8jlHHQ3s9O059Fc3zRDzMmVKcpYfpU+3oI/umxJyH+TYqLxUPc0X13xVqMMovFQ8zpPIbon6M
WCoeZljVMUz9VIqz9DAP1Dt6QP0a9gpZ7+lhHhXjysreaOhhfiv1vaGH+T2Mv5rbU+hh/uAaOnlN
Xv+Hy4/7mtv3OW5hnpTODIYe5mm0xqbiYf4OcbLv08NU1ZyuuqKLOEvm6sjhJkd8TjRustgkrO3u
vFGjh60r1uyiPHrY6eH84tb7l/SwM8vrAT3snHgNY9wcsoby+Y8edn5UxxTxsIuitrlcFpG9GcVx
/6CHXRrKk72MHrYl3stYB/ceu7I4X02wlWSrCmaF1ehhV7NrovWKHrattI4betj20Fc8r7E87kf2
g+gcy32BHnZDfKZmHPco2xnl4vqlk2yz6r/N1EfRPpiKh90d7VGpeNi9inGPst2lNdbSwx4McS8k
7iDVE/Ytz3qoXsV6qZOKnaTOBDYqjPuRPRfOkz7uHNUf4uQMQg/7XekMYulhB6JnE/GwP0T1JuJh
ryrGM6G9HuWSiIcdDnPmhTs70sPeCuPes1vUXcXuUvcDGxV2n/olOisn4mEfhfOVby/3KDsSlZeI
h32iGOe0faoY57R9ptgzajTKJREPOx7aJnOfHhUbxov0Mz0qU8v50aMyo/wu6VGZrdhsqqH8fnll
HEEz4zj6DNMxK+4X+gyv8cszyoU+4zfmjNAO9zuXrNGXF1gj2ULFFpI1K9ZMtiww//22jGwFXg39
535XkK0O+cl5gz7Du6iP5wd9hvfDs9LP9BnWR/U6tp6sU7FOsi1RLo5tIdsWled+t5HtVO3YSdal
WBfZftW2/WQHVH4HyA6F9+GfPUR2VOV3lKxXsV6yE4qdIDul2Cmys6ptZ8n6Qi7+m7OP7ELoU/8t
dIHsoo8L+V0ku6xyvkw2qNgg2VBgvg+GyK6XyrP0GW5ydE3EuXd5k+xOeOdVibtD9jNm/Qv15O4i"""

# courbB08.pbm font file uuencoded
courB08_pbm ="""eJxNkntM01cUx8+P2/1apUAZEpECq4KRjKhF0E55FYEp4yG6mglz2Q8Q1BhERhhls/zKI+CID4wb
IAPKpk4GAzqZPKKMX2GIUwGJG+ImtKwKjIzXcGuBtncV0Hn+uLnn5Nzv55xv7mdRkbusVjquBACr
0N3B+wCQi/m+ijAf4LGl/wgAiwkNDpRIyyABSjGkBQ/fa3c1bfLs4U8ulDcYUs/502rTpIlO9pyc
Kp/Buql6f3rmZ1NqvpO2SZXf0duY3j0563zjoZpW8AvHRmVeZ/Co36mFR8bERzlsxOMJ+oJshsS5
7rlfzFzmnZFEFnIEZjTGizgLsLzjl4QtrNprBRu10e+u9GgePHjG63bPDw/H87uix0Vtsvkqg9qO
lUimPLiOM4z69YfqIu5Pa2Sr/io6n9Xmf9e+57W1Iapo4lLQBdLSWc/z3KOSlgznDXTW/Flh21kX
IeUIX8FZVL9dwP4NBH5jglYxkBNFmWgMcfsAxM/9gEL5TTwYpnfElR8qQ+WiCgeTHOAfb2bW/cQC
/FozFOOQzAebtjRvQLI7HBtXvaZe25a3Q/1vZpPa+kd1XXKuflr5Cm48YUsUcjMXjsm/sf+22s6z
QAbGZ8mEXMzSE4y9AHhRpltwB1N9ynz5H2MOi0MEi4E5O1ov9ogrFU5cMWAcdgQb3xHFtFK+0pkh
VnYWxltx92j69p6jJ9OnHr+Cq5x5X6Mz70JcX2tEG5LIShM4EHIGoLIRsHzcvEuGwMYA4DZPn7gP
MA1QIgltnt82cTu7j5n76mmz3TU5Bh3PFRTHku52aBgaTnJD7m1c0a3hNjbWWjBtMsP/OFac/LYA
NAAWepdYodB58NBFIuOjNSQ4cgXplqP2RyOe8fd999T8weqBRwLwNFdQobHgA1/YTV8PH+TwV59v
Bo7Y1J4rmHFv3T9e8rmmXdGSuPpSbBnhYJ7V8ICz6AfGcdTpRkpCUU8WcOT8wb+dSHIb6QZapx0M
Y2DO4i7jYV2AUNkkErpQFHVYmFRmYD7OJhDyQSiow4IkrS3TbpQqFA9slE4jnj6peXMTC+N8buJ2
0Uv5eOothuGIiluyCDtff3miBzJHjncOIC3bPT8FLabRPd0TCWy346Mmn9Rz23WyNMJcsnqhQani
3CMFOZuYU7c20zTNVqNbGPNxALWnybeLEcTvXWpc10leI5ae/CI9qBqI686cnO6P6F33e2vAp0nz
9+hnbNeueh/261UJK5aVeSf73ZSXA7dOBXvkXODEb9hVww4KtPNAbPvaZbi0q9kICCl+CiBJSzLv
a8TlntYlC4UHvCRTlaXOy13VAbN0eae2v3hNesWXLsWPkjfOPq7e6zd1fOfc1TckDaylrvleinnT
8Ui87ScLMVhhEx7SUJ8U2zKrRR2Z1dEqZlkr7kDTuhFjpkvse9ZXN0R9H+DlYA4TXVm6/kXDQMyT
eGnJFXlLlSgva5iLUEcbiyDzNqf4Wr9kKYVUIcY40DrnsW4E4zW9QxnHVYx+bo64mIskDWjZgCrq
eVQFrS7Sh/uFLftIidKWbgj6Oq652d4c3v88Dw2JDK7bSWX/ByuaLZI="""


def GetCode128C(inputdate):
    bits = ""
    checksum = 105
    j = 1
    for index, a in enumerate(inputdate):
        if (index % 2 == 0):
            checksum += int(inputdate[index: index+2].rstrip()) * j
            if (int(inputdate[index: index+2]) < 95):
                bits += str(int(inputdate[index: index+2]) + 32)
            else:
                bits += str(int(inputdate[index: index+2]) + 100)
            j += 1
        index += 1
    checksum = checksum % 103
    if (checksum < 95):
        checksum += 32
    else:
        checksum += 100
    bits = str(205) + bits + str(checksum) + str(206)
    # Create a missing font file
    decodeFontFile(courB08_pil ,"courB08.pil")
    decodeFontFile(courB08_pbm ,"courB08.pbm")
    position = 8
    im = Image.new("1",(len(bits)+position,50))
    # Load font
    font = ImageFont.load("courB08.pil")

      
    # Create drawer
    draw = ImageDraw.Draw(im)
    # Erase image
    draw.rectangle(((0,0),(im.size[0],im.size[1])),fill=256)
      
      # Draw first part of number
    draw.text((0, 50-9), "hello", font=font, fill=0)
      
      # Draw first part of number
    draw.text((position+7, 50-9), "hello", font=font, fill=0)
         
      # Draw second part of number
    draw.text((len(bits)/2+6+position, 50-9), "hello", font=font, fill=0)
    
    # Erase image
    draw.rectangle(((0,0),(im.size[0],im.size[1])),fill=256)
    for bit in range(len(bits)):
        # Draw normal bar
        if bits[bit] == '1':
            draw.rectangle(((bit+position,0),(bit+position,50-10)),fill=0)
        # Draw long bar
        elif bits[bit] == 'L':
            draw.rectangle(((bit+position,0),(bit+position,50-3)),fill=0)
            
      # Save the result image
    im.save(inputdate+"."+lower("png"), upper("png"))
    #print(result)



def decodeFontFile(data, file):
   """ Decode font file embedded in this script and create file """
   from zlib import decompress
   from base64 import decodestring
   from os.path import exists
   
   # If the font file is missing
   if not exists(file):
      # Write font file
      open (file, "wb").write(decompress(decodestring(data)))


'''
使用huBarcode,pygame和PIL生成条形码
'''
if __name__ == "__main__":
   GetCode128C("444993846033")