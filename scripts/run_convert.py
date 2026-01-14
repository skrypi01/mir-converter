from mir_converter.xlsx_to_csv import convert_xlsx_to_csv

if __name__ == "__main__":
    result = convert_xlsx_to_csv(
        xlsx_path="c:\\Users\\irs31342\\OneDrive - Groupe IPSEN\\Documents\\data\\MIR_20240930.xlsx",
        csv_path="c:\\Users\\irs31342\\OneDrive - Groupe IPSEN\\Documents\\data\\MIR_20240930_clean.csv"
    )
    print("Conversion complete:")
    print(result)
