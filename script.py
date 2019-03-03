highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)
highlighted_poems_stripped = []
for highlighted_poems in highlighted_poems_list:
  highlighted_poems_stripped.append(highlighted_poems.strip())
print(highlighted_poems_stripped)
highlighted_poems_details = []
for highlighted_poems in highlighted_poems_stripped:
  highlighted_poems_details.append(highlighted_poems.split(':'))
titles = []
poets = []
dates = []
for highlighted_poems in highlighted_poems_details:
  titles.append(highlighted_poems[0])
  poets.append(highlighted_poems[1])
  dates.append(highlighted_poems[2])
for index in range(len(titles)):
  print("The Poem {} was published by {} in {}".format(titles[index],poets[index],dates[index]))

  