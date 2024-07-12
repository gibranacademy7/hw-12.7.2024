
# קולט ערכים ומחשבת ממוצע IQ של קבוצת הביקורת לפני הלימודים
iq_list_before = [];
iq = int(input("Enter the pre-school IQ value of the group: "));
while 30 <= iq <= 300:
    iq_list_before.append(iq);
    iq = int(input("Enter the pre-school IQ value of the group: "));

if len(iq_list_before) > 0:
    avg_iq_before = sum(iq_list_before) / len(iq_list_before);
    print(f"The average IQ of the group before school is: {avg_iq_before}");
else:
    print("No valid pre-school IQ values were entered");

print("A year of Python studies is complete...");

# קולט ערכים ומחשב ממוצע IQ של קבוצת הביקורת אחרי הלימודים
iq_list_after = []
iq = int(input("Enter the IQ value of the group after school: "));
while 30 <= iq <= 300:
    iq_list_after.append(iq)
    iq = int(input("Enter the IQ value of the group after school: "));

if len(iq_list_after) > 0:
    avg_iq_after = sum(iq_list_after) / len(iq_list_after);
    print(f" The average IQ of the group after school is: {avg_iq_after}");
    if len(iq_list_before) > 0:
        print(f"The average increased by: {avg_iq_after - avg_iq_before}");
else:
    print("No valid post-school IQ values were entered.");
