import pygal

data_file = "data.txt"
LIMIT = 12.3

LV0 = 9500000
LV1 = 9800000
LV2 = 10000000
DVS1 = 300000
DVS2 = 200000
TOPC = 30
def calc_ptt(difficulty, score):
  if score < LV1:
    return max(0.0, difficulty + (score - LV0) * 1.0 / DVS1)
  if score < LV2:
    return difficulty + 1 + (score - LV1) * 1.0 / DVS2
  return difficulty + 2
def get_color(mind, interval, diff):
  r = (diff - mind) / interval
  return (0 * (1 - r) + 138 * r,
          199 * (1 - r) + 43 * r,
          140 * (1 - r) + 226 * r)

if __name__ == "__main__":
  file = open(data_file, "r")
  songs = []
  mind = 12.1
  maxd = 0
  while True:
    line = file.readline()[:-1]
    if not line:
      break
    data = line.split()
    diff = float(data[1])
    if calc_ptt(diff, int(data[2])) < LIMIT:
      continue
    songs.append((calc_ptt(diff, int(data[2])), diff, data[0].replace('_', ' ')))
    mind = min(mind, diff)
    maxd = max(maxd, diff)
  interval = maxd - mind
  if interval < 0.1:
    interval = 0.1
  file.close()
  songs.sort()
  
  ptt = [{
      "value": song[0], 
      "color": "grey" if len(songs) - i > TOPC
                      else "rgb(%f, %f, %f)" % get_color(mind, interval, song[1])
      } for (i, song) in enumerate(songs)]
  titles = ["%.1f %s #%d" % (song[1], song[2], len(songs) - i)
            for (i, song) in enumerate(songs)]
  
  chart = pygal.Line(
    style = pygal.style.DarkGreenBlueStyle,
    show_legend = False,
    x_label_rotation = 40,
    truncate_label = -1,
    )
  chart.title = "Arcaea PTT Table"
  chart.x_labels = titles
  chart.add("ptt", ptt)
  chart.render_to_file("table.svg")
  
  output = open("table.txt", "w")
  for song in songs[::-1]:
    output.write("%.1f %.4f %s\n" % (song[1], song[0], song[2]))
  output.close()
  