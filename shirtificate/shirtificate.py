from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Configurar a fonte para o cabeçalho (topo do PDF)
        self.set_font("helvetica", "B", 45)
        # Criar uma célula centralizada com o título
        self.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

def main():
    name = input("Name: ")
    generate_shirtificate(name)

def generate_shirtificate(name):
    # Instanciar a classe com orientação Retrato (P) e formato A4
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Adicionar a imagem da camisa
    # Largura do A4 é 210mm. Uma camisa de 170mm centralizada começa em x=20
    pdf.image("shirtificate.png", x=20, y=70, w=170)

    # Configurar o texto branco para o nome sobre a camisa
    pdf.set_font("helvetica", "B", 25)
    pdf.set_text_color(255, 255, 255)

    # Posicionar o cursor para escrever o nome dentro da camisa
    # y=140 é aproximadamente a parte superior/peito da camisa na imagem
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # Gerar o arquivo final
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
