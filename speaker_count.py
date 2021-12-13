"""
Last Update: Dec 2021
Note:
1) Remember to add +1 on the terms count every semester for students not in internships;
2) Check list of presenters on the website.
"""

import collections
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=1.3)
sns.set_style("whitegrid")

presenters = ['Shuman',
              'Mehrdad',
              'Ali',
              'Lai',
              'Raquel',
              'Raquel',
              'Shuman',
              'Atia',
              'Oliver',
              'Shuman',
              'Arash',
              'Oliver',
              'Atia',
              'Lai',
              'Raquel',
              'Shuman',
              'Arash',
              'Lai',
              'Oliver',
              'Shuman',
              'Atia',
              'Martin',
              'Arash',
              'Raquel',
              'Atia',
              'Lai',
              'Oliver',
              'Shuman',
              'Andy',
              'Shuman',
              'Oliver',
              'Andy',
              'Shuman',
              'Shuman',
              'Raquel',
              'Oliver',
              'Atia',
              'Oliver',
              'Shuman',
              'Lai',
              'Arash',
              'Oliver',
              'Mehrdad',
              'Shuman',
              'Ali',
              'Raquel',
              'Arash',
              'Atia',
              'Martin',
              'Ali'
              ]

terms = {'Ali': 6,  # two internships
         'Andy': 5,
         'Arash': 7,
         'Atia': 7,
         'Lai': 6,  # internship
         'Martin': 8,
         'Mehrdad': 6,  # stuck in Australia
         'Oliver': 8,
         'Raquel': 6,  # two internships
         'Shuman': 8,
         }

c = collections.Counter(presenters)
c = sorted(c.items())

name = [freq[0] for freq in c]
count = [freq[1] for freq in c]
prop = [freq[1] / terms[freq[0]] for freq in c]

fig, (ax0, ax1) = plt.subplots(ncols=1, nrows=2, figsize=[14, 14])  # )

sns.barplot(ax=ax0, x=name, y=count, color='#1e90ff', dodge=False)
ax0.set(xlabel='', ylabel='Frequency')
ax0.set_title('a. Total Presentations', fontsize=14)

sns.barplot(ax=ax1, x=name, y=prop, color='#1e90ff', dodge=False)
ax1.set(xlabel='', ylabel='Frequency')
ax1.set_title('b. Presentations/Active Semesters', fontsize=14)
