from util.hfss_script import HFSS

model_dx = "2mm"
model_dy = "2mm"



app = HFSS()
app.new_project()
app.new_hfss_design("test_design")