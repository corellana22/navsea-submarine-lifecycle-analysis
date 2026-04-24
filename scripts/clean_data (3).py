"""
Orion Georgiou 
11/24/25
Clean data on submarine lifecycles
Update1: swap the dates whenever the start date occurs after the end date
Update2: add ship names based on its hull number
"""

import pandas as pd

df = pd.read_csv("submarine_lifecycle.csv")
print("Segment of original data: \n", df.head())


# for consistency
for column in ["Location", "Ship Class", "Period Type"]:
    for row in range(len(df)):
        value = df.loc[row, column]
        
        if pd.notna(value):
            value = value.strip().title()
            df.loc[row, column] = value


# To make state abbv capitalized
for row in range(len(df)):
    loc = df.loc[row, "Location"]
    
    if isinstance(loc, str) and "," in loc: # accounts for empty slots; only focuses on strings
        city_state = loc.split(",")
        if len(city_state[-1].strip()) == 2:
            city_state[-1] = city_state[-1].strip().upper()
            df.loc[row, "Location"] = ", ".join(city_state)



# to accnt for diff formats of dates, goes through 2 tests
# copies of original, used for test 2
start_original = df["Start Date"].copy()
end_original   = df["End Date"].copy()

# Test 1: month/day/year
df["Start Date"] = pd.to_datetime(start_original, errors="coerce", dayfirst=False) # coerce : error -> NaT
df["End Date"]   = pd.to_datetime(end_original,   errors="coerce", dayfirst=False)

# NaT r placeholders, fixed here:
# Test 2: day/month/year
missing_start = df["Start Date"].isna()
df.loc[missing_start, "Start Date"] = pd.to_datetime(start_original[missing_start], errors="coerce", dayfirst=True)

missing_end = df["End Date"].isna()
df.loc[missing_end, "End Date"] = pd.to_datetime(end_original[missing_end], errors="coerce", dayfirst=True)


#new
# to fix the rows where start date is after end date
date_issue = df["Start Date"] > df["End Date"]
total_date_issue = date_issue.sum()
# swap 
df.loc[date_issue, ["Start Date", "End Date"]] = df.loc[date_issue, ["End Date", "Start Date"]].to_numpy()
print("fixed", total_date_issue, "rows where start Date was after end Date.")

# to confirm
still = df["Start Date"] > df["End Date"]
if still.any():
    print("\nerror NOT fixed.")
else:
    print("Error fixed.")


# organizes data by hull num and date (other possibility is to instead sort it chronologically)
df = df.sort_values(by=['Hull Number', 'Start Date']).reset_index(drop=True)

# based on data, ones with missing locations are at Period Type: "At Sea"
at_sea = df["Period Type"].str.strip().str.lower() == "at sea"
missing_loc = df["Location"].isna()
df.loc[at_sea & missing_loc, "Location"] = "Sea"


# for missing ship class (assuming they are constant for the hull number)
for row in range(len(df)):
    if pd.isna(df.loc[row, "Ship Class"]):  
        hull = df.loc[row, "Hull Number"]  
        # any other row with same hull num which contains a ship class
        match = df[df["Hull Number"] == hull]["Ship Class"].dropna()
        
        if not match.empty:
            df.loc[row, 'Ship Class'] = match.iloc[0]  # copy the first one found

# remove duplicate rows: 
with_duplicates = len(df)
df = df.drop_duplicates(keep="first")  # keeps one (1st that shows up), drops others

removed = with_duplicates - len(df)
print(f"Got rid of {removed} duplicate rows.")


#NEW2
ship_name_file = pd.read_csv("submarine_names.csv")
#clean names
ship_name_file["Ship Name"] = ship_name_file["Ship Name"].astype(str).str.strip()
ship_name_file["Hull Number"] = ship_name_file["Hull Number"].astype(str).str.strip().str.upper()

#dictionary: {Hull Number, Ship Name}
dictionary = dict(zip(ship_name_file["Hull Number"], ship_name_file["Ship Name"]))

#clean original file hull num (maybe optional)
df["Hull Number"] = df["Hull Number"].astype(str).str.strip().str.upper()

# add new column
df["Ship Name"] = df["Hull Number"].map(dictionary)

print("Empty info for:")
print("Start Date:", df["Start Date"].isna().sum())
print("End Date:",   df["End Date"].isna().sum())
print("Location:",   df["Location"].isna().sum())
print("Ship Class:", df["Ship Class"].isna().sum())
print("Ship Name:", df["Ship Name"].isna().sum())

out_path = "submarine_lifecycle_cleaned2.csv"
df.to_csv(out_path, index=False)
print(f"\nSaved to: {out_path}")
print("\nSegment of cleaned data:\n", df.head())

# EOF