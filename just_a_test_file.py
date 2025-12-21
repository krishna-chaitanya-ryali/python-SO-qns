# Sample data
d = [
    {'NEW_ID': 721, 'NEWS_SUBJECT': 'ONE SUBJECT', 'RMM_ID': 1, 'NEWS_ORDER': 1, 'NEWS_TYPE': 0},
    {'NEW_ID': 722, 'NEWS_SUBJECT': 'ONE SUBJECT', 'RMM_ID': 2, 'NEWS_ORDER': 1, 'NEWS_TYPE': 0},
    {'NEW_ID': 740, 'NEWS_SUBJECT': 'TWO SUBJECT', 'RMM_ID': 1, 'NEWS_ORDER': 2, 'NEWS_TYPE': 0},
    {'NEW_ID': 741, 'NEWS_SUBJECT': 'TWO SUBJECT', 'RMM_ID': 2, 'NEWS_ORDER': 2, 'NEWS_TYPE': 0},
    {'NEW_ID': 750, 'NEWS_SUBJECT': 'Three SUBJECT', 'RMM_ID': 1, 'NEWS_ORDER': 3, 'NEWS_TYPE': 0},
    {'NEW_ID': 751, 'NEWS_SUBJECT': 'Three SUBJECT', 'RMM_ID': 2, 'NEWS_ORDER': 3, 'NEWS_TYPE': 0}
]

# Step 1: Identify and remove subjects with duplicate NEWS_ORDER for RMM_ID 1 and 2
subjects_to_remove = set()

# Check for duplicate NEWS_ORDER values for the same NEWS_SUBJECT
for subject in set(item['NEWS_SUBJECT'] for item in d):
    orders_for_subject = set()
    for item in [i for i in d if i['NEWS_SUBJECT'] == subject]:
        if item['NEWS_ORDER'] in orders_for_subject:
            subjects_to_remove.add(subject)
            break
        orders_for_subject.add(item['NEWS_ORDER'])

# Step 2: Filter out items for subjects that should be removed
d_filtered = [item for item in d if item['NEWS_SUBJECT'] not in subjects_to_remove]

# Step 3: Sort the filtered data by NEWS_SUBJECT and NEWS_ORDER
d_filtered.sort(key=lambda x: (x['NEWS_SUBJECT'], x['NEWS_ORDER']))

# Step 4: Reassign NEWS_ORDER to the remaining items (1, 1, 2, 2, etc.)
for index, item in enumerate(d_filtered):
    item['NEWS_ORDER'] = index + 1  # Starting from 1

# Output the result
for item in d_filtered:
    print(item)
