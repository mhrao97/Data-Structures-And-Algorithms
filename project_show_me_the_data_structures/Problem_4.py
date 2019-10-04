# Problem 4 - Active Directory

import sys
sys.path.append("c:/Users/M/Anaconda3/Lib/site-packages/")

# Your work here

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user == None:
        print("No user to look for")
        return False

    if group == None:
        print("No group to check membership against")
        return False

    for group_user in group.get_users():
        if group_user == user:
            return True

    for sub_group in group.get_groups():
        return is_user_in_group(user, sub_group)

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

admin = Group("admin")
admin.add_user(admin)

ro = Group("read-only")
ro.add_user(ro)

super_user = "superuser"
parent.add_user(super_user)

print("Case where group is None...\n")
print("checking is_user_in_group(super_user, None)? ", is_user_in_group(super_user, None))

print("\nCase where user is None...\n")
print("checking is_user_in_group(None, admin)? ", is_user_in_group(None, admin))

print("\nOther test cases...\n")
print("checking is_user_in_group(super_user, parent)? ", is_user_in_group(super_user, parent))
print("checking is_user_in_group(super_user, sub_child)? ", is_user_in_group(super_user, sub_child))

print("checking is_user_in_group(sub_child_user, parent)? ", is_user_in_group(sub_child_user, parent))
print("checking is_user_in_group(child, parent)? ", is_user_in_group(child, parent))
print("checking is_user_in_group(sub_child_user, child)? ", is_user_in_group(sub_child_user, child))

print("checking is_user_in_group(ro, admin)? ", is_user_in_group(ro, admin))
print("checking is_user_in_group(admin, admin)? ", is_user_in_group(admin, admin))

# the above test cases should print the following:
"""
Case where group is None...

No group to check membership against
checking is_user_in_group(super_user, None)?  False

Case where user is None...

No user to look for
checking is_user_in_group(None, admin)?  False

Other test cases...

checking is_user_in_group(super_user, parent)?  True
checking is_user_in_group(super_user, sub_child)?  False
checking is_user_in_group(sub_child_user, parent)?  True
checking is_user_in_group(child, parent)?  False
checking is_user_in_group(sub_child_user, child)?  True
checking is_user_in_group(ro, admin)?  False
checking is_user_in_group(admin, admin)?  True

"""