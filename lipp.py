from tkinter import *

# Loome peamise akna
raam = Tk()
raam.title("Lääne-Nigula lipp")

# Loome tahvli laiusega 880px ja kõrgusega 560px
tahvel = Canvas(raam, width=880, height=560)

# Valge taust
tahvel.create_rectangle(0, 0, 880, 560, fill="white", outline="white")

# Ülemine valge riba (1/5 lehest)
tahvel.create_rectangle(0, 0, 880, 112, fill="white", outline="white")

# Roheline riba (keskmine osa)
tahvel.create_rectangle(0, 112, 880, 448, fill="green", outline="green")

# Alumine valge riba (1/5 lehest)
tahvel.create_rectangle(0, 448, 880, 560, fill="white", outline="white")

# Ristikheina sümbol
# Määrame ristikheina asukoha
x_offset = 146.67  # Vasakule nihutatud, et jääks 1/6 lehe suurusest vahe
y_offset = 280      # Keskel vertikaalselt

# Ristikheina lehed (suurendatud)
leaf_size = 40  # Suur leht

# Suur leht keskel
tahvel.create_oval(
    x_offset - leaf_size, y_offset - leaf_size,  # Suure lehe ülemine vasak nurk
    x_offset + leaf_size, y_offset + leaf_size,   # Suure lehe alumine parem nurk
    fill="white", outline="black"
)

# Vasak leht (väiksem)
tahvel.create_oval(
    x_offset - leaf_size * 1.5, y_offset - leaf_size * 0.5,  # Vasak ülemine nurk
    x_offset - leaf_size * 0.5, y_offset + leaf_size * 0.5,   # Parempoolne alumine nurk
    fill="white", outline="black"
)

# Parem leht (väiksem)
tahvel.create_oval(
    x_offset + leaf_size * 0.5, y_offset - leaf_size * 0.5,  # Vasak ülemine nurk
    x_offset + leaf_size * 1.5, y_offset + leaf_size * 0.5,   # Parempoolne alumine nurk
    fill="white", outline="black"
)

# Ülemine leht (väiksem)
tahvel.create_oval(
    x_offset - leaf_size * 0.5, y_offset - leaf_size * 1.5,  # Vasak ülemine nurk
    x_offset + leaf_size * 0.5, y_offset - leaf_size * 0.5,   # Parempoolne alumine nurk
    fill="white", outline="black"
)

# Alumine leht (väiksem)
tahvel.create_oval(
    x_offset - leaf_size * 0.5, y_offset + leaf_size * 0.5,  # Vasak ülemine nurk
    x_offset + leaf_size * 0.5, y_offset + leaf_size * 1.5,   # Parempoolne alumine nurk
    fill="white", outline="black"
)

# Lisame punase risti keskele
cross_size = 20  # Risti suurus
tahvel.create_line(
    x_offset - cross_size, y_offset,  # Horisontaalne joon
    x_offset + cross_size, y_offset,
    fill="red", width=3
)
tahvel.create_line(
    x_offset, y_offset - cross_size,  # Vertikaalne joon
    x_offset, y_offset + cross_size,
    fill="red", width=3
)

# Paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()

# Siseneme põhitsüklisse
raam.mainloop()