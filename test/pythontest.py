from pdf_compressor import compress
print("Hello from inside the container!")

compress("Hindustan Times 04072020.pdf", "compressed.pdf", power=4)
