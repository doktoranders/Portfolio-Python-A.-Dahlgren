#Enter the cost of food and how much it will cost with and without tipping

def number_cruncher(amount, cost_without_tip, tip):
    per_capita_cost_no_tip = cost_without_tip / amount
    total_price_with_tipping = cost_without_tip * (1 + tip / 100)
    per_capita_cost_with_tipping = total_price_with_tipping / amount
    return per_capita_cost_no_tip, total_price_with_tipping, per_capita_cost_with_tipping

amount = int(input('How many are you? '))
cost_without_tip = int(input('What did the food cost without tip? '))
tip = int(input('How much will you leave in tip? '))
per_capita_cost_no_tip, total_price_with_tipping, per_capita_cost_with_tipping = number_cruncher(amount, cost_without_tip, tip)
print('The food price without tipping:', cost_without_tip)
print('Per capita cost with no tip:', per_capita_cost_no_tip)
print('Total cost with tipping:', total_price_with_tipping)
print('Per capita cost with tipping:', per_capita_cost_with_tipping)