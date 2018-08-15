from textwrap import dedent
# import sys
from uuid import uuid4


WIDTH = 80
ORDER_COMPLETE = False
TAX_RATE = float('.096')
TOTAL = float('0')
CATEGORIES = ['appetizers', 'entrees', 'sides', 'drinks', 'desserts']
BANK = [
  {
    'category': 'desserts',
    'item': 'brownie',
    'ammount': 1,
    'price': 1.95,
    'order': 0,
  },
  {
    'category': 'desserts',
    'item': 'pudding',
    'ammount': 1,
    'price': 2.50,
    'order': 0,
  },
  {
    'category': 'desserts',
    'item': 'cream and fruit',
    'ammount': 1,
    'price': 5.50,
    'order': 0,
  },
  {
    'category': 'drinks',
    'item': 'pop',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'category': 'drinks',
    'item': 'lemonade',
    'ammount': 1,
    'price': 1.5,
    'order': 0,
  },
  {
    'category': 'drinks',
    'item': 'milk shake',
    'ammount': 1,
    'price': 5.59,
    'order': 0,
  },
  {
    'category': 'sides',
    'item': 'french fries',
    'ammount': 1,
    'price': 3.5,
    'order': 0,
  },
  {
    'category': 'sides',
    'item': 'asparagus',
    'ammount': 1,
    'price': 3.75,
    'order': 0,
  },
  {
    'category': 'sides',
    'item': 'pig strips',
    'ammount': 1,
    'price': 4.25,
    'order': 0,
  },
  {
    'category': 'entrees',
    'item': 'creature of unknown origin',
    'ammount': 1,
    'price': 25.95,
    'order': 0,
  },
  {
    'category': 'entrees',
    'item': 'tortured baby cow',
    'ammount': 1,
    'price': 16.25,
    'order': 0,
  },
  {
    'category': 'appetizers',
    'item': 'spinach artichoke dip',
    'ammount': 1,
    'price': 4.25,
    'order': 0,
  },
  {
    'category': 'appetizers',
    'item': 'jalapeno poppers',
    'ammount': 1,
    'price': 3.5,
    'order': 0,
  },
  {
    'category': 'appetizers',
    'item': 'mozzarella sticks',
    'ammount': 1,
    'price': 3.5,
    'order': 0,
  },
  {
    'category': 'sides',
    'item': 'corn on the cob',
    'ammount': 1,
    'price': 3.25,
    'order': 0,
  },
  {
    'category': 'sides',
    'item': 'garlic mashed potatoes',
    'ammount': 1,
    'price': 3.25,
    'order': 0,
  },
  {
    'category': 'sides',
    'item': 'broccoli',
    'ammount': 6,
    'price': 3,
    'order': 0,
  },
  {
    'category': 'appetizers',
    'item': 'wings',
    'ammount': 6,
    'price': 3,
    'order': 0,
  },
  {
    'category': 'appetizers',
    'item': 'cookies',
    'ammount': 3,
    'price': 1.5,
    'order': 0,
  },
  {
    'category': 'appetizers',
    'item': 'spring rolls',
    'ammount': 4,
    'price': 2,
    'order': 0,
  },
  {
    'category': 'entrees',
    'item': 'salmon',
    'ammount': 1,
    'price': 15,
    'order': 0,
  },
  {
    'category': 'entrees',
    'item': 'steak',
    'ammount': 1,
    'price': 18,
    'order': 0,
  },
  {
    'category': 'entrees',
    'item': 'meat tornado',
    'ammount': 1,
    'price': 13,
    'order': 0,
  },
  {
    'category': 'entrees',
    'item': 'a little garden',
    'ammount': 1,
    'price': 3.5,
    'order': 0,
  },
  {
    'category': 'desserts',
    'item': 'ice cream',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'category': 'desserts',
    'item': 'cake',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'category': 'desserts',
    'item': 'pie',
    'ammount': 1,
    'price': 2.50,
    'order': 0,
  },
  {
    'category': 'drinks',
    'item': 'coffee',
    'ammount': 1,
    'price': .75,
    'order': 0,
  },
  {
    'category': 'drinks',
    'item': 'tea',
    'ammount': 1,
    'price': .75,
    'order': 0,
  },
  {
    'category': 'drinks',
    'item': 'blood of the innocent',
    'ammount': 1,
    'price': 6.66,
    'order': 0,
  },
]


def greeting():
  # multi line string
  """Function which will greet the user when the application executes for 
  the first time.
  """
  ln_one = 'Welcome to the Snakes Cafe!'
  ln_two = 'Please see our menu below.'
  ln_three = 'To quit at any time, type "quit"'

  print(dedent(f'''
    {'*' * WIDTH}
    {'**' + (' ' * (((WIDTH - 2) - len(ln_one)) // 2)) + ln_one + (' ' * (((WIDTH - 4) - len(ln_one)) // 2)) + '**'}
    {'**' + (' ' * (((WIDTH - 4) - len(ln_two)) // 2)) + ln_two + (' ' * (((WIDTH - 4) - len(ln_two)) // 2)) + '**'}
    {'**' + (' ' * (WIDTH - 4)) + '**'}
    {'**' + (' ' * (((WIDTH - 4) - len(ln_three)) // 2)) + ln_three + (' ' * (((WIDTH - 4) - len(ln_three)) // 2)) + '**'}
    {'*' * WIDTH}
  '''))


def List_Category(category):
  print(dedent(f'''
    {category}
    {'-' * len(category)}'''))
  for menue in BANK:
    item = menue['item']
    price = "%.2f" % round(float(menue['price']),2)
    space = (' ' * (WIDTH - (len(item) + len(str(price)) + 2)))
    if category == menue['category']:
      print(dedent(f'''{item + space + ' $' + str(price)}'''))


def Message():
  ln_message = 'What would you like to order?'
  print(dedent(f'''
    {'*' * WIDTH}
    {'**' + (' ' * (((WIDTH - 2) - len(ln_message)) // 2)) + ln_message + (' ' * (((WIDTH - 4) - len(ln_message)) // 2)) + '**'}
    {'*' * WIDTH}
  '''))


def Manual():
  ln_zero = 'Manual'
  ln_one = 'Type "Category" to bring up a list of category options.'
  ln_two = 'Type the name of the category to see the menue items in that category.'
  ln_three = 'Type the name of the menue item you would like to add to the order.'
  ln_five = 'At any time you can type "quit" or "exit" to stop the application.'
  ln_four = 'type "order" to print current order to screen.'

  print(dedent(f'''
    {ln_zero}
    {'-' * len(ln_zero)}
    {ln_one}
    {ln_two}
    {ln_three}
    {ln_four}
    {ln_five}
  '''))


def exit():
  print(dedent(f'''
  Thank you for using snakes cafe!
  '''))
  # sys.exit()

def complete():
  print(dedent(f'''
  {'_' * WIDTH}
  {'The Snakes Cafe'}
  {"Eatability Counts"}
  {''}
  {'Order: ' + str(uuid4())}
  {'=' * WIDTH}'''))
  subtotal = float('0')
  for menue in BANK:
    item = menue['item']
    order = menue['order']
    price = str("%.2f" % round(float(menue['order']) * float(menue['price']),2))
    space = (' ' * (WIDTH - (len(item) + len(str(order)) + len(str(price) + '    '))))
    if menue['order'] > 0:
      subtotal = float(price) + subtotal
      print(dedent(f'''{item + ' x' + str(order) + space + ' $' + str(price)}'''))
  sales_tax = float(subtotal) * TAX_RATE
  total_due = float(subtotal) + float(sales_tax)
  print(dedent(f'''
  {'*' * WIDTH}
  {'Subtotal: ' + (' ' * (40 - (len(str(subtotal)) + 12))) + '$' + str("%.2f" % float(subtotal))}
  {'Sales Tax: ' + (' ' * (40 - (len(str(sales_tax)) + 12))) + '$' + str("%.2f" % float(sales_tax))}
  {'=' * 40}
  {'Total Due: ' + (' ' * (40 - (len(str(total_due)) + 12))) + '$' + str("%.2f" % float(total_due))}
  {'_' * WIDTH}
  '''))



def run():
  greeting()
  for key in CATEGORIES:
    List_Category(key)
  Message()
  while ORDER_COMPLETE == False:
    order = input().lower()
    if order == 'quit' or order == 'exit':
      exit()
      return
    elif order == 'man' or order == 'help':
      Manual()
    for menue in BANK:
      if order == menue['category']:
        List_Category(order)
        print('')
        break
    if order == 'category':
      print('-' * len(order))
      for key in CATEGORIES:
        print(key)
    for menue in BANK:
      price = "%.2f" % round(float(menue['price']),2)
      if order == menue['item']:
        menue['order'] = menue['order'] + 1
        print(menue['order'], 'order(s) of', order, 'at $' + str(price) , ' have been added to your meal.')
        global TOTAL
        TOTAL = float(price) + TOTAL
        print('Current Total W/O tax: $' + str("%.2f" % round(float(TOTAL),2)))
      elif order == 'order':
        complete()
        break
      else:
        continue


if __name__ == '__main__':
  run()
