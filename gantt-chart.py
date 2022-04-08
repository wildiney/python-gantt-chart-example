#!/usr/bin/env python3
# http://xael.org/pages/python-gantt-en.html

import datetime
import gantt

chart_name = input("Insert the chart name:")

gantt.define_font_attributes(
    fill='black', stroke='black', stroke_width=0, font_family="Verdana")
gantt.define_not_worked_days([5, 6])

CI = gantt.Resource("CI")
CRI = gantt.Resource("CRI")
PUB = gantt.Resource("PUB")

mc = gantt.Project(name="First Project")
mc.add_task(gantt.Task(name="Planning", start=datetime.date(
    2018, 1, 8),  duration=3, percent_done=10))
mc.add_task(gantt.Task(name="Creation",
                       start=datetime.date(2018, 1, 11), duration=7))
mc.add_task(gantt.Task(name="Divulgation",
                       start=datetime.date(2018, 1, 19), duration=2))
mc.add_task(gantt.Task(name="Participation", start=datetime.date(
    2018, 1, 22), stop=datetime.date(2018, 2, 13)))
mc.add_task(gantt.Task(name="Vote",
                       start=datetime.date(2018, 2, 14), duration=3))
mc.add_task(gantt.Task(name="Premiation",
                       start=datetime.date(2018, 2, 19), duration=4))

dm = gantt.Project(name="Second Project")
dm.add_task(gantt.Task(name="Planning",
                       start=datetime.date(2018, 4, 30), duration=3))
dm.add_task(gantt.Task(name="Divulgation",
                       start=datetime.date(2018, 5, 9), duration=3))
dm.add_task(gantt.Task(name="Premiation",
                       start=datetime.date(2018, 5, 11), duration=1))


pg = gantt.Project(name="2018")
pg.add_task(mc)
pg.add_task(dm)

pg.make_svg_for_tasks(filename="charts/"+chart_name+".svg")
