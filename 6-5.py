#slices string and turns it into an integer

text = "X-DSPAM-Confidence:    0.8475";

pos = text.find("0")
ext = text[(pos):]
float(ext)
print ext
