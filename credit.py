import re


def mask_cc_number(cc_string, digits_to_keep=4, mask_char='*'):
   cc_string_total = sum(map(str.isdigit, cc_string))

   if len(Credit_Card) != 16:
      print("Invalid Credit Card number.")
   if len(Credit_Card) == 16:
      digits_to_mask = cc_string_total - digits_to_keep
      masked_cc_string = re.sub('\d', mask_char, cc_string, digits_to_mask)

      return masked_cc_string

Credit_Card=input("Enter any Credit Card number: ")

print(mask_cc_number(Credit_Card))


