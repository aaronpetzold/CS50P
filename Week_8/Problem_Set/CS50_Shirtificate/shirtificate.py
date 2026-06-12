from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add shirtificate.png image
    pdf.image(
        r"C:\Users\aaron\Documents\CS50P\Week_8\Problem_Set\CS50_Shirtificate\shirtificate.png",
        x=30,
        y=60,
        w=150,
    )

    # Black "CS50 Shirtificate" Title
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", style="B", size=40)
    pdf.set_y(30)
    pdf.cell(0, 10, "CS50 Shirtificate", align="C")

    # White name on Shirt
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", style="B", size=24)
    pdf.set_y(100)
    pdf.cell(0, 10, name, align="C")

    # Save
    pdf.output(
        r"C:\Users\aaron\Documents\CS50P\Week_8\Problem_Set\CS50_Shirtificate\shirtificate.pdf"
    )


if __name__ == "__main__":
    main()
