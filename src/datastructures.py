
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "Pau",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22],
        },
        {
            "id": self._generateId(),
            "first_name": "Yoel",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3],
        },
        {
            "id": self._generateId(),
            "first_name": "Daniel",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1],
        },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        inner_member = {
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"],
            "id": self._generateId(),
        }
        self._members.append(inner_member)
        return inner_member
    
    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member ["id"] == id:
                self._members.remove(member)
                return {"message": "Member deleted successfully"}
        return {"error": "Member not found"}

    def get_member(self, id):
      for member in self._members:
          if member["id"] == id:
              return member
      return None

    def update_member(self, id, updated_member):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                for key, value in updated_member.items():
                    if key in self._members[i]:
                        self._members[i][key] = value
                return {"message": "Member updated successfully", "updated_member": updated_member}

        return {"error": "Member not found"}

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members   