import json

class RestAPI:
  def __init__(self, database=None):
    self.users = database['users'] or []


  def get(self, url, payload=None):
    if not payload:
      return json.dumps({"users": self.users})

    data = json.loads(payload)
    names = data['users']

    filtered = [
      user
      for user in self.users
      if user['name'] in names
    ]

    filtered.sort(key=lambda x: x['name'])

    return json.dumps({"users": filtered})


  def post(self, url, payload=None):
    if url == "/add":
      return self.post_user(payload)

    if url == "/iou":
      return self.post_iou(payload)


# =====================================================================
# ADD USER
# =====================================================================
  def post_user(self, payload):
    data = json.loads(payload)
    name = data['user']

    user = {
      "name": name,
      "owes": {},
      "owed_by": {},
      "balance": 0.0
    }

    self.users.append(user)
    return json.dumps(user)


# =====================================================================
# IOU LOGIC
# =====================================================================
  def post_iou(self, payload):
    data = json.loads(payload)

    lender_name = data['lender']
    borrower_name = data['borrower']
    amount = data['amount']

    lender = self.find_user(lender_name)
    borrower = self.find_user(borrower_name)

    # Case 1: Borrower already owes lender --> inrease debt
    if lender_name in borrower['owes']:
      borrower['owes'][lender_name] += amount
      lender['owed_by'][borrower_name] += amount

    # Case 2: Lender owes borrower --> decrease debt
    elif borrower_name in lender['owes']:
      debt = lender['owes'][borrower_name]

      if debt > amount:
        lender['owes'][borrower_name] -= amount
        borrower['owed_by'][lender_name] -= amount

      elif debt < amount:
        new_debt = amount - debt

        del lender['owes'][borrower_name]
        del borrower['owed_by'][lender_name]

        borrower['owes'][lender_name] = new_debt
        lender['owed_by'][borrower_name] = new_debt

      elif debt == amount:
        del lender['owes'][borrower_name]
        del borrower['owed_by'][lender_name]

    # Case 3: No previous debt
    else:
      borrower['owes'][lender_name] = amount
      lender['owed_by'][borrower_name] = amount

    # Recompute balances
    self.update_balance(lender)
    self.update_balance(borrower)

    users = sorted([lender, borrower], key=lambda x: x['name'])

    return json.dumps({"users": users})



# =====================================================================
# HELPERS
# =====================================================================
  def find_user(self, username):
    for user in self.users:
      if user['name'] == username:
        return user


  def update_balance(self, user):
    owed = sum(user['owed_by'].values())
    owes = sum(user['owes'].values())
    user['balance'] = owed - owes
