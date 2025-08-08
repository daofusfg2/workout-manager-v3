from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.clock import Clock
from kivy.lang import Builder



KV_FILE = """
<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: 'vertical'
        Button:
            id: add_workout_btn
            text: "Add workout"
            background_color: 0.1, 0.1, 0.1, 1
            on_release: app.root.current = "workout"
            font_size: 28

        Button:
            id: view_workout_btn
            text: "View workout"
            background_color: 0.1, 0.1, 0.1, 1
            on_release: app.root.current = "ViewWorkout"
            font_size: 28
        Button:
            id: ach_btn
            text: "Achievements"
            background_color: 0.1, 0.1, 0.1, 1
            on_release: app.root.current = "ASCREEN"   
            font_size: 28
        Button:
            id: settings_btn
            text: "Settings"
            background_color: 0.1, 0.1, 0.1, 1
            on_release: app.root.current = "settings" 
            font_size: 28
<SettingsScreen>:
    name: "settings"
    BoxLayout:
        orientation: 'vertical'

        Label:
            id: white_mode_label
            text: "White Mode"


        Switch:
            id: white_switch
            on_active: root.activate_white_mode(self)
            size_hint_y: .5
            height: '40dp'
            color: 1,1,1,1
        Label:
            id: lbs_mode_label
            text: "LBS Mode"
        Switch:
            id: lbs_switch
            on_active: root.activate_lbs_mode(self)
            size_hint_y: .5
            height: '40dp'
        Button:
            id: font_size_btn
            text: "Font Size"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "change_font_screen"
        Button:
            id: saveandback_btn
            text: "Save and Back"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "main"   

<change_font_screen>:
    name: "change_font_screen"
    ScrollView:
        scroll_type: ['bars', 'content']
        #bar_width: '5dp'
        #bar_color: 0, 0.7, 0.7, 1
        #bar_inactive_color: 0, 0.7, 0.7, 0.5

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height

            Button:
                id: f11
                text: "11"
                font_size: 16
                size_hint_y: None
                height: 400
                on_press: root.f11()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f12
                text: "12"
                font_size: 17
                size_hint_y: None
                height: 400
                on_press: root.f12()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f13
                text: "13"
                font_size: 18
                size_hint_y: None
                height: 400
                on_press: root.f13()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f14
                text: "14"
                font_size: 19
                size_hint_y: None
                height: 400
                on_press: root.f14()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f15
                text: "15"
                font_size: 20
                size_hint_y: None
                height: 400
                on_press: root.f15()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f16
                text: "16"
                font_size: 21
                size_hint_y: None
                height: 400
                on_press: root.f16()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f17
                text: "17"
                font_size: 22
                size_hint_y: None
                height: 400
                on_press: root.f17()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f18
                text: "18"
                font_size: 23
                size_hint_y: None
                height: 400
                on_press: root.f18()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f19
                text: "19"
                font_size: 24
                size_hint_y: None
                height: 400
                on_press: root.f19()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f20
                text: "20"
                font_size: 25
                size_hint_y: None
                height: 400
                on_press: root.f20()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f21
                text: "21"
                font_size: 26
                size_hint_y: None
                height: 400
                on_press: root.f21()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f22
                text: "22"
                font_size: 27
                size_hint_y: None
                height: 400
                on_press: root.f22()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f23
                text: "23"
                font_size: 28
                size_hint_y: None
                height: 400
                on_press: root.f23()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f24
                text: "24"
                font_size: 29
                size_hint_y: None
                height: 400
                on_press: root.f24()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f25
                text: "25"
                font_size: 30
                size_hint_y: None
                height: 400
                on_press: root.f25()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f26
                text: "26"
                font_size: 31
                size_hint_y: None
                height: 400
                on_press: root.f26()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f27
                text: "27"
                font_size: 32
                size_hint_y: None
                height: 400
                on_press: root.f27()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f28
                text: "28"
                font_size: 33
                size_hint_y: None
                height: 400
                on_press: root.f28()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f29
                text: "29"
                font_size: 34
                size_hint_y: None
                height: 400
                on_press: root.f29()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f30
                text: "30"
                font_size: 35
                size_hint_y: None
                height: 400
                on_press: root.f30()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f40
                text: "40"
                font_size: 45
                size_hint_y: None
                height: 400
                on_press: root.f40()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f50
                text: "50"
                font_size: 55
                size_hint_y: None
                height: 400
                on_press: root.f50()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f60
                text: "60"
                font_size: 65
                size_hint_y: None
                height: 400
                on_press: root.f60()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f70
                text: "70"
                font_size: 75
                size_hint_y: None
                height: 400
                on_press: root.f70()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f80
                text: "80"
                font_size: 85
                size_hint_y: None
                height: 400
                on_press: root.f80()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: f90
                text: "90"
                font_size: 95
                size_hint_y: None
                height: 400
                on_press: root.f90()
                background_color: 0.1, 0.1, 0.1, 1
            Button:
                id: back_btn
                text: "<-- Back -->"
                size_hint_y: None
                height: 400
                on_release: app.root.current = "settings"
                background_color: 0.1, 0.1, 0.1, 1
                font_size: 25


<ViewWorkout>:
    name: "ViewWorkout"
    BoxLayout:
        orientation: 'vertical'

        Label:
            id: comp_text
            text: ""
            width: self.width

        Label:
            id: total_reps
            text: ""
            font_size: 53

        Label:
            id: total_minutes
            text: ""
            font_size: 50

        Label:
            id: total_weight
            text: ""
            font_size: 51
        
        Label:
            id: total_workout_count
            text: ""
            font_size: 52

        Button:
            id: refresh_world
            text: "Refresh Stats"
            on_press: root.ddo()
            background_color: 0.1, 0.1, 0.1, 1
        Button:
            id: back_btn
            text: "<-- Back -->"
            on_release: app.root.current = "main"
            background_color: 0.1, 0.1, 0.1, 1
<WorkoutScreen>:
    name: "workout"
    BoxLayout:

        orientation: 'vertical'
        Button:
            id: chest_workout
            text: "| Chest workout |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "ChestWorkout"
        Button:
            id: trap_workout
            text: "| Trap workout |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "TrapWorkout"
        Button:
            id: back_workout
            text: "| Back workout |"
            background_color: 0.1, 0.1, 0.1, 1 
            font_size: 40
            on_release: app.root.current = "BackWorkout"
        Button:
            id: shoulder_workout
            text: "| Shoulders workouts |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "ShoulderWorkout"
        Button:
            id: bicep_workout
            text: "| Bicep workouts |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "BicepWorkout"
        Button:
            id: forearm_workout
            text: "| Forearm workouts |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "ForearmWorkout"
        Button:
            id: abs_workout
            text: "| Abs workouts |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "AbsWorkout" 
            font_name: "Roboto"
        Button:
            id: quads_workout
            text: "| Quads workouts |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "QuadsWorkout" 
            font_name: "Roboto"
        Button:
            id: hamgstring_workout
            text: "| Hamstring workouts |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "HamstringWorkout" 
            font_name: "Roboto"
        Button:
            id: calves_workout
            text: "| Calves workouts |"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 40
            on_release: app.root.current = "CalvesWorkout" 
            font_name: "Roboto"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 50
            on_release: app.root.current = "main"
            font_name: "Roboto"            
<ChestWorkout>:
    name: "ChestWorkout"
    BoxLayout:
        orientation: 'vertical'
        Button:
            id: Barbell_Bench_Press
            text: "Barbell Bench Press"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: Cable_Crossover
            text: "Cable Crossover"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: Chest_Dips
            text: "Chest Dips"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: Decline_Bench_Press
            text: "Decline Bench Press"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: Decline_Push_Up
            text: "Decline Push-Up"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: Dumbbell_Bench_Press
            text: "Dumbbell Bench Press"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: Dumbell_Flyes
            text: "Dumbbell Flyes"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: Incline_Bench_Press
            text: "Incline Bench Press"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
            font_name: "Roboto"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "workout"
            font_name: "Roboto"
<BackWorkout>:
    name: "BackWorkout"
    BoxLayout:
        orientation: 'vertical'
        Button:
            id: Barbell_Shrug
            text: "Barbell Row"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Bent_Over_Row
            text: "Bent-Over Row"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Cable_Row
            text: "Cable Row (Seated)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Deadlift
            text: "Deadlift"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Dumbell_Row
            text: "Dumbell Row (Single arm)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Face_Pull
            text: "Face Pull"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Inverted_Row
            text: "Inverted Row"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Lat_Pulldown
            text: "Lat Pulldown"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Pull_Up
            text: "Pull-Up"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Rack_Pull
            text: "Rack Pull"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Seated_Row
            text: "Seated Row (Machine or Cable)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Wide_Grip_Pull_Up
            text: "Wide-Grip Pull-Up"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "workout"
<BicepWorkout>:
    name: "BicepWorkout"
    BoxLayout:
        orientation: 'vertical'
        Button:
            id: Barbell_Curl
            text: "Barbell Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Dumbell_Curl
            text: "Dumbbell Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Hammer_Curl
            text: "Hammer Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Preacher_Curl
            text: "Preacher Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Concentration_Curl
            text: "Concentration Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Incline_Dumbell_Curl
            text: "Incline Dumbbell Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Cable_Curl
            text: "Cable Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: EzBar_Curl
            text: "EZ-Bar Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Chin_Up
            text: "Chin-Up"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Zottman_Curl
            text: "Zottman Curl"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 27
            on_release: app.root.current = "workout"
<TrapWorkout>:
    name: "TrapWorkout"
    
    BoxLayout:
        orientation: 'vertical'
        Button:
            id: Barbell_Shrug
            text: "Barbell Shrug"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: BTB_Barbell_Shrug
            text: "Behind-the-back Barbell Shrug"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Cable_Face_Pull
            text: "Cable Face Pull"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Dumbell_Shrug
            text: "Dumbbell Shrug"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Farmers_Carry
            text: "Farmer's Carry"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: High_Pull
            text: "High Pull"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Machine_Shrug
            text: "Machine Shrug"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Rack_Pull
            text: "Rack Pull"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Smith_Machine_Shrug
            text: "Smith Machine Shrug"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Trap_Bar_Shrug
            text: "Trap Bar Shrug"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Upright_Row
            text: "Upright Row"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Y_Raise
            text: "Y Raise (Prone or on incline)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "workout"
<ShoulderWorkout>:
    name: "ShoulderWorkout"

    BoxLayout:
        orientation: 'vertical'
        
        Button:
            id: Overhead_Press
            text: "Overhead Press (Barbell or Dumbbell)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Arnold_Press
            text: "Arnold Press"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Lateral_Raises
            text: "Lateral Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Front_Raises
            text: "Front Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Rear_Delt_Flyes
            text: "Rear Delt Flyes (Reverse Flyes)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Face_Pulls
            text: "Face Pulls"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Push_Press
            text: "Push Press"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Upright_Rows
            text: "Upright Rows"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Cable_Lateral_Raises
            text: "Cable Lateral Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Rack_Pulls
            text: "Rack Pulls"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 26
            on_release: app.root.current = "workout"
<ForearmWorkout>:
    name: "ForearmWorkout"
    BoxLayout:
        orientation: 'vertical'

        Button:
            id: Wrist_Curls
            text: "Wrist Curls"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Reverse_Wrist_Curls
            text: "Reverse Wrist Curls"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Hammer_Curls
            text: "Hammer Curls"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Reverse_Curls
            text: "Reverse Curls (Ez-Bar or Barbell)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Farmers_Carry
            text: "Farmer's Carry / Farmer's Walk"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Wrist_Roller
            text: "Wrist Roller"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Dead_Hangs
            text: "Dead Hangs"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Plate_Pinch_Hold
            text: "Plate Pinch Hold"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Towel_Pulls_Up
            text: "Towel Pull-Ups"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Barbell_Holds
            text: "Barbell Holds"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 26
            on_release: app.root.current = "workout"
<QuadsWorkout>:
    name: "QuadsWorkout"

    BoxLayout:
        orientation: 'vertical'

        Button:
            id: Squats
            text: "Squats"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Front_Squats
            text: "Front Squats"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Leg_Press
            text: "Leg Press"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Lunges
            text: "Lunges"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Bulgarian_Split_Squats
            text: "Bulgarian Split Squats"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Step_Ups
            text: "Step-Ups"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Leg_Extensions
            text: "Leg Extensions"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Hack_Squats
            text: "Hack Squats"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Goblet_Squats
            text: "Goblet Squats"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Sissy_Squats
            text: "Sissy Squats"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 26
            on_release: app.root.current = "workout"
<HamstringWorkout>:
    name: "HamstringWorkout"

    BoxLayout:
        orientation: 'vertical'

        Button:
            id: Romanian_Deadlifts
            text: "Romanian Deadlifts"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Stiff_Leg_Deadlift
            text: "Stiff-Leg Deadlifts"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Conventional_Deadlifts
            text: "Conventional Deadlifts"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Good_Mornings
            text: "Good Mornings"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Lying_Leg_Curls
            text: "Lying Leg Curls (Machine)"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Seated_Leg_Curls_Machine
            text: "Seated Leg Curls Machine"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Nordic_Hamstring_Curls
            text: "Nordic Hamstring Curls"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Glute_Ham_Raises
            text: "Glute-Ham Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Cable_Leg_Curls
            text: "Cable Leg Curls"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Kettlebell_Swings
            text: "Kettlebell Swings"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 26
            on_release: app.root.current = "workout"
<CalvesWorkout>:
    name: "CalvesWorkout"
    BoxLayout:
        orientation: 'vertical'

        Button:
            id: Standing_Calf_Raises
            text: "Standing Calf Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Seated_Curl_Raises
            text: "Seated Calf Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Donkey_Calf_Raises
            text: "Donkey Calf Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Single_Leg_Calf_Raises
            text: "Single Leg Calf Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Leg_Press_Calf_Raises
            text: "Leg Press Calf Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Smith_Machine_Calf_Raises
            text: "Smith Machine Calf Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Farmers_Walk_On_Toes
            text: "Farmer's Walk on Toes"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Jump_Rope
            text: "Jump Rope"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Box_Jumps
            text: "Box Jumps"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: TipToe_Walks
            text: "TipToe Walks"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 26
            on_release: app.root.current = "workout"
<AbsWorkout>:
    name: "AbsWorkout"

    BoxLayout:
        orientation: 'vertical'

        Button:
            id: Crunches
            text: "Crunches"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Sit_Ups
            text: "Sit-Ups"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Leg_Raises
            text: "Leg Raises"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Plank
            text: "Plank"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Bycicle_Crunches
            text: "Bycicle Crunches"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Russian_Twists
            text: "Russian Twists"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Mountain_Climbers
            text: "Mountain Climbers"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id:  V_Ups
            text: "V-Ups"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Flutter_Kicks
            text: "Flutter Kicks"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: Toe_Touches
            text: "Toe Touches"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "AddWorkout"
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 26
            on_release: app.root.current = "workout"
<ASCREEN>:
    name: "ASCREEN"
    BoxLayout:
        orientation: 'vertical'

        Label:
            id: reps_100
            text: "Do 100 reps of any exersize. (Uncompleted)"
            color: 1, 0, 0, 1
            #size_hint: 1, .1
        Label:
            id: minutes_60
            text: "Workout for a total of an hour. (Uncompleted)"
            color: 1, 0, 0, 1
        Label:
            id: lift_500
            text: "Lift a total of 500KG. (Uncompleted)"
            color: 1, 0, 0, 1
        Label:
            id: lift_1200
            text: "Lift as much as a normal car. (1200KG) (Uncompleted)"
            color: 1, 0, 0, 1
        Label:
            id: do_10
            text: "Do 10 Workouts. (Uncompleted)"
            color: 1, 0, 0, 1
        Label:
            id: hours_10
            text: "Work out for a total of 10 hours. (Uncompleted)"
            color: 1, 0, 0, 1
        Label:
            id: workouts_100
            text: "Do a total of 100 workouts. (Uncompleted)"
            color: 1, 0, 0, 1
         
        Button:
            id: back_btn
            text: "<-- Back -->"
            background_color: 0.1, 0.1, 0.1, 1
            font_size: 48
            on_release: app.root.current = "main"
<AddWorkout>:
    name: "AddWorkout"
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: err_label
            text: ""
            size_hint: 0,0
        Label:
            text: "How many reps did you do?"
            font_size: 48
        TextInput:
            id: tot_reps
            input_filter: 'int'
            multiline: False
        #Label:
        #    text: " "
        #    font_size: 25
        Label:
            text: "How many total minutes did your workout take?"
        TextInput:
            id: tot_min
            input_filter: 'int'
            multiline: False
        Label:
            text: "What is the weight that you repped?"
        TextInput:
            id: tot_weight
            input_filter: 'int'
            multiline: False
        Button:
            id: add_btn
            text: "Add"
            on_press: root.counter()
            background_color: 0, 0, 0, 1
        Button:
            id: back_btn
            text: "<-- Back -->"
            on_release: app.root.current = "workout"
            background_color: 0, 0, 0, 1
<ScreenManagerApp>:
    MainScreen:
    SettingsScreen:
    WorkoutScreen:
    ViewWorkout:
    ChestWorkout:
    AddWorkout:
    ASCREEN:
    TrapWorkout:
    BackWorkout:
    ShoulderWorkout
    BicepWorkout:
    ForearmWorkout:
    AbsWorkout:
    QuadsWorkout
    HamstringWorkout:
    CalvesWorkout:
    change_font_screen:

"""

Builder.load_string(KV_FILE)
with open("logs.json", "r") as file:
    data = json.load(file)




class WorkoutScreen(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.chest_workout_setw, 0)
            Clock.schedule_once(self.trap_workout_setw, 0)
            Clock.schedule_once(self.back_workout_setw, 0)
            Clock.schedule_once(self.shoulder_workout_setw, 0)
            Clock.schedule_once(self.bicep_workout_setw, 0)
            Clock.schedule_once(self.forearm_workout_setw, 0)
            Clock.schedule_once(self.abs_workout_setw, 0)
            Clock.schedule_once(self.quads_workout_setw, 0)
            Clock.schedule_once(self.hamstring_workout_setw, 0)
            Clock.schedule_once(self.calves_workout_setw, 0)
            Clock.schedule_once(self.back_btn_setw, 0)
    def chest_workout_setw(self, dt):
        btn = self.ids["chest_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def trap_workout_setw(self, dt):
        btn = self.ids["trap_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_workout_setw(self, dt):
        btn = self.ids["back_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def shoulder_workout_setw(self, dt):
        btn = self.ids["shoulder_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def bicep_workout_setw(self, dt):
        btn = self.ids["bicep_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def forearm_workout_setw(self, dt):
        btn = self.ids["forearm_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def abs_workout_setw(self, dt):
        btn = self.ids["abs_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def quads_workout_setw(self, dt):
        btn = self.ids["quads_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def hamstring_workout_setw(self, dt):
        btn = self.ids["hamgstring_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def calves_workout_setw(self, dt):
        btn = self.ids["calves_workout"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn_setw(self, dt):
        btn4 = self.ids["back_btn"]
        btn4.background_color = (1, 1, 1, 1)
        btn4.background_normal = ''
        btn4.color = (0, 0, 0, 1)
class MainScreen(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.set_white_button, 0)
            Clock.schedule_once(self.set_white_button2, 0)
            Clock.schedule_once(self.set_white_button3, 0)
            Clock.schedule_once(self.set_white_button4, 0)
        elif data["white_mode"] is False:
            Clock.schedule_once(self.set_black_button, 0)
            Clock.schedule_once(self.set_black_button2, 0)
            Clock.schedule_once(self.set_black_button3, 0)
            Clock.schedule_once(self.set_black_button4 , 0)
    def set_white_button(self, dt):
        btn = self.ids["add_workout_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
        self.ids.add_workout_btn.font_size = data["font_size"]

    def set_white_button2(self, dt):
        btn = self.ids["view_workout_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
        self.ids.view_workout_btn.font_size = data["font_size"]

    def set_white_button3(self, dt):
        btn = self.ids["ach_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
        self.ids.ach_btn.font_size = data["font_size"]

    def set_white_button4(self, dt):
        btn = self.ids["settings_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
        self.ids.settings_btn.font_size = data["font_size"]

    def set_black_button(self, dt):
        btn = self.ids["add_workout_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
        self.ids.add_workout_btn.font_size = data["font_size"]

    def set_black_button2(self, dt):
        btn = self.ids["view_workout_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
        self.ids.view_workout_btn.font_size = data["font_size"]
    def set_black_button3(self, dt):
        btn = self.ids["ach_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
        self.ids.ach_btn.font_size = data["font_size"]
    def set_black_button4(self, dt):
        btn = self.ids["settings_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
        self.ids.settings_btn.font_size = data["font_size"]

    
class ASCREEN(Screen):
    def on_enter(self):
        if data["white_mode"] == True:
            Clock.schedule_once(self.back_btn_sw, 0)
        if data["white_mode"] == False:
            Clock.schedule_once(self.back_btn_sb, 0)

        if data["tot_reps"] >= 100:
            self.ids.reps_100.color = (0, 1, 0, 1)
            self.ids.reps_100.text = f"Do 100 reps of any exersize. (Completed)"
        if data["tot_min"] >= 60:
            self.ids.minutes_60.color = (0, 1, 0, 1)
            self.ids.minutes_60.text = f"Workout for a total of an hour. (Completed)"
        if data["tot_weight"] >= 500:
            self.ids.lift_500.color = (0, 1, 0, 1)
            self.ids.lift_500.text = f"Lift a total of 500KG. (Completed)"
        if data["tot_weight"] >= 1200:
            self.ids.lift_1200.color = (0, 1, 0, 1)
            self.ids.lift_1200.text = f"Lift as much as a normal car. (1200KG) (Completed)"
        if data["workouts_done"] >= 10:
            self.ids.do_10.color = (0, 1, 0, 1)
            self.ids.do_10.text = f"Do 10 Workouts. (Completed)"
        if data["tot_min"] >= 600:
            self.ids.do_10.color = (0, 1, 0, 1)
            self.ids.do_10.text = f"Work out for a total of 10 hours. (Completed)" 
        if data["workouts_done"] >= 100:
            self.ids.do_10.color = (0, 1, 0, 1)
            self.ids.do_10.text = f"Do a total of 100 workouts. (Completed)" 
        
    def back_btn_sw(self, dt):
        btn4 = self.ids["back_btn"]
        btn4.background_color = (1, 1, 1, 1)
        btn4.background_normal = ''
        btn4.color = (0, 0, 0, 1)
    def back_btn_sb(self, dt):
        btn4 = self.ids["back_btn"]
        btn4.background_color = (0, 0, 0, 1)
        btn4.background_normal = ''
        btn4.color = (1, 1, 1, 1)

class SettingsScreen(Screen):
    def on_enter(self):
            if data["white_mode"] == True:
                self.ids.white_switch.active = True
            if data["white_mode"] == False:
                self.ids.white_switch.active = False

            if data["lbs_mode"] == True:
                self.ids.lbs_switch.active = True
            if data["lbs_mode"] == False:
                self.ids.lbs_switch.active = False
            
            
            if data["white_mode"] is True:
                Clock.schedule_once(self.font_size_btn_set_white, 0)
            if data["white_mode"] is True:
                Clock.schedule_once(self.saveandback_btn_set_white, 0)

            if data["white_mode"] is False:
                Clock.schedule_once(self.font_size_btn_set_black, 0)

            if data["white_mode"] is False:
                Clock.schedule_once(self.saveandback_btn_set_black, 0)

    def font_size_btn_set_white(self, widget):
        btn = self.ids["font_size_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
        self.ids.white_mode_label.background_color = (1, 1, 1, 1)


    def saveandback_btn_set_white(self, widget):
        btn = self.ids["saveandback_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

    def activate_white_mode(self, widget):
        if widget.active == True:
            data["white_mode"] = True
            with open("logs.json", "w") as file:
                json.dump(data, file)
        if widget.active == False:
            data["white_mode"] = False
            with open("logs.json", "w") as file:
                json.dump(data, file)



    def font_size_btn_set_black(self, widget):
        btn = self.ids["font_size_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)


    
    def saveandback_btn_set_black(self, widget):
        btn = self.ids["saveandback_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)

    def activate_white_mode(self, widget):
        if widget.active == True:
            data["white_mode"] = True
            with open("logs.json", "w") as file:
                json.dump(data, file)
        if widget.active == False:
            data["white_mode"] = False
            with open("logs.json", "w") as file:
                json.dump(data, file)















    def activate_lbs_mode(self, widget):
        if widget.active == True:
            data["lbs_mode"] = True
            # lbs_weight = data["tot_weight"] * 2.2
            # data["tot_weight"]  = lbs_weight
            
            with open("logs.json", "w") as file:
                json.dump(data, file)
        if widget.active == False:
            data["lbs_mode"] = False

            with open("logs.json", "w") as file:
                json.dump(data, file)

class AddWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
                Clock.schedule_once(self.add_btn_cw, 0)
                Clock.schedule_once(self.back_btn_cw)

        if data["white_mode"] is False:
                Clock.schedule_once(self.add_btn_cb, 0)
                Clock.schedule_once(self.back_btn_cb, 0)

    def add_btn_cw(self, widget):
        btn = self.ids["add_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn_cw(self, widget):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

    def add_btn_cb(self, widget):
        btn = self.ids["add_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def back_btn_cb(self, widget):
        btn = self.ids["add_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)




    def counter(self):
        global user_input
        tot_reps = self.ids.tot_reps.text
        tot_min = self.ids.tot_min.text
        tot_weight = self.ids.tot_weight.text
        
        new_number = int(tot_reps) * int(tot_weight)


        data["tot_reps"] += int(tot_reps)
        
        data["tot_min"] += int(tot_min)
        data["tot_weight"] += new_number
        data["workouts_done"] += 1

        with open("logs.json", "w") as file:
            json.dump(data, file)


class ViewWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
                Clock.schedule_once(self.refresh_world_cw, 0)
                Clock.schedule_once(self.back_btn, 0)
        if data["white_mode"] is False:
                Clock.schedule_once(self.refresh_world_cb, 0)
                Clock.schedule_once(self.back_btn_cb, 0)
        

    def refresh_world_cw(self, widget):
        btn = self.ids["refresh_world"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

    def back_btn(self, widget):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

    def refresh_world_cb(self, widget):
        btn = self.ids["refresh_world"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)

    def back_btn_cb(self, widget):
        btn = self.ids["back_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)


    def ddo(self):


        self.ids.total_reps.text = f"You done a total of: {data['tot_reps']} reps."

        self.ids.total_minutes.text = f"You have worked out a total of: {data['tot_min']} minutes."
        if self.ids.total_minutes.font_size >= 50:
            self.ids.total_minutes.font_size = data["font_size"] - 5

        if data["lbs_mode"] == True:
            
            self.ids.total_weight.text = f"You have lifted a total of: {data['tot_weight'] * 2} LBS."
            if self.ids.total_minutes.font_size > 50:
                self.ids.total_minutes.font_size = data["font_size"] - 5

        if data["lbs_mode"] == False:
            self.ids.total_weight.text = f"You have lifted a total of: {data['tot_weight']} kilos."
            if self.ids.total_weight.font_size > 50:
                self.ids.total_weight.font_size = data["font_size"] - 3

        self.ids.total_workout_count.text = f"You have done a total of {data['workouts_done']} workouts."
        if self.ids.total_workout_count.font_size > 50:
            self.ids.total_workout_count.font_size = data["font_size"] - 3

        if data["tot_weight"] >= 5 and data["tot_weight"] <= 20:
            self.ids.comp_text.text = f"You've (In Total) Lifted A TV"
            self.ids.comp_text.width = self.width

        if data["tot_weight"] >= 20 and data["tot_weight"] <= 50:
            self.ids.comp_text.text = f"You've (In Total) Lifted a A Giant Pacific Octopus."
            self.ids.comp_text.width = self.width

        if data["tot_weight"] >= 51 and data["tot_weight"] <= 70:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Small motorcycle."
            self.ids.comp_text.width = self.width

        if data["tot_weight"] >= 71 and data["tot_weight"] <= 100:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Motorcycle engine."

            self.ids.comp_text.width = self.width

        if data["tot_weight"] >= 101 and data["tot_weight"] <= 150:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Lion (female or adolescent male)."


            self.ids.comp_text.width = self.width

        if data["tot_weight"] >= 151 and data["tot_weight"] <= 200:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Harley-Davidson Sportster, Or a giant Panda."

            self.ids.comp_text.width = self.width

        if data["tot_weight"] >= 201 and data["tot_weight"] <= 300:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Adult black bear."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 301 and data["tot_weight"] <= 400:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Grizzly bear, Or a silverback Gorrila, Or an Adult female horse."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 401 and data["tot_weight"] <= 500:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Adult cow, Or male horse, Polarbear or Adult Tiger/Lion."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 501 and data["tot_weight"] <= 700:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Adult male moose, Or a Small compact car."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 701 and data["tot_weight"] <= 1000:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Adult bull, Or a large draft horse, Or a water buffalo, Or a small shipping container."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 1001 and data["tot_weight"] <= 1500:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Bison, Or a young elephant, Or a mini excavator, Or a small to mid size car."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 1501 and data["tot_weight"] <= 2000:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Adult female african elephant, Or a Adult asian elephant, Or a rhino, Or a SUV."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 2001 and data["tot_weight"] <= 4000:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Adult male African elephant, Or a Hippo, Or a Large rhino, Or a Girrafe (Adult male), Or a pickup truck."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 4001 and data["tot_weight"] <= 6000:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Ambulance, Or a large delivery truck, Or a African bush elephant"

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 6001 and data["tot_weight"] <= 8000:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Walrus, Or a Armored SWAT vehicle, Or a large white rhino."

            self.ids.comp_text.width = self.width
        if data["tot_weight"] >= 8001 and data["tot_weight"] <= 10000:
            self.ids.comp_text.text = f"You've (In Total) Lifted a Medium-duty trucks fully loaded, Or a Full-size RV, Or a Mobile crane base (small model)."

            self.ids.comp_text.width = self.width

class ChestWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Barbell_Bench_Press, 0)
            Clock.schedule_once(self.Cable_Crossover, 0)
            Clock.schedule_once(self.Chest_Dips, 0)
            Clock.schedule_once(self.Decline_Bench_Press, 0)
            Clock.schedule_once(self.Decline_Push_Up, 0)
            Clock.schedule_once(self.Dumbbell_Bench_Press, 0)
            Clock.schedule_once(self.Dumbell_Flyes, 0)
            Clock.schedule_once(self.Incline_Bench_Press, 0)
            # Clock.schedule_once(self.cdsd, 0)
            Clock.schedule_once(self.back, 0)


    def Barbell_Bench_Press(self, dt):
        btn = self.ids["Barbell_Bench_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Cable_Crossover(self, dt):
        btn = self.ids["Cable_Crossover"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Chest_Dips(self, dt):
        btn = self.ids["Chest_Dips"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Decline_Bench_Press(self, dt):
        btn = self.ids["Decline_Bench_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Decline_Push_Up(self, dt):
        btn = self.ids["Decline_Push_Up"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Dumbbell_Bench_Press(self, dt):
        btn = self.ids["Dumbbell_Bench_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Dumbell_Flyes(self, dt):
        btn = self.ids["Dumbell_Flyes"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Incline_Bench_Press(self, dt):
        btn = self.ids["Incline_Bench_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class TrapWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Barbell_Shrug, 0)
            Clock.schedule_once(self.BTB_Barbell_Shrug, 0)
            Clock.schedule_once(self.Cable_Face_Pull, 0)
            Clock.schedule_once(self.Dumbell_Shrug, 0)
            Clock.schedule_once(self.Farmers_Carry, 0)
            Clock.schedule_once(self.High_Pull, 0)
            Clock.schedule_once(self.Machine_Shrug, 0)
            Clock.schedule_once(self.Rack_Pull, 0)
            Clock.schedule_once(self.Smith_Machine_Shrug, 0)
            Clock.schedule_once(self.Trap_Bar_Shrug, 0)
            Clock.schedule_once(self.Upright_Row, 0)
            Clock.schedule_once(self.Y_Raise, 0)
            Clock.schedule_once(self.back_btn, 0)
    def Barbell_Shrug(self, dt):
        btn = self.ids["Barbell_Shrug"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def BTB_Barbell_Shrug(self, dt):
        btn = self.ids["BTB_Barbell_Shrug"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Cable_Face_Pull(self, dt):
        btn = self.ids["Cable_Face_Pull"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Dumbell_Shrug(self, dt):
        btn = self.ids["Dumbell_Shrug"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Farmers_Carry(self, dt):
        btn = self.ids["Farmers_Carry"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def High_Pull(self, dt):
        btn = self.ids["High_Pull"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Machine_Shrug(self, dt):
        btn = self.ids["Machine_Shrug"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Rack_Pull(self, dt):
        btn = self.ids["Rack_Pull"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Smith_Machine_Shrug(self, dt):
        btn = self.ids["Smith_Machine_Shrug"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Trap_Bar_Shrug(self, dt):
        btn = self.ids["Trap_Bar_Shrug"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Upright_Row(self, dt):
        btn = self.ids["Upright_Row"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Y_Raise(self, dt):
        btn = self.ids["Y_Raise"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class ShoulderWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Overhead_Press, 0)
            Clock.schedule_once(self.Arnold_Press, 0)
            Clock.schedule_once(self.Lateral_Raises, 0)
            Clock.schedule_once(self.Front_Raises, 0)
            Clock.schedule_once(self.Rear_Delt_Flyes, 0)
            Clock.schedule_once(self.Face_Pulls, 0)
            Clock.schedule_once(self.Push_Press, 0)
            Clock.schedule_once(self.Upright_Rows, 0)
            Clock.schedule_once(self.Cable_Lateral_Raises, 0)
            Clock.schedule_once(self.Rack_Pulls, 0)
            Clock.schedule_once(self.back_btn, 0)
    
    def Overhead_Press(self, dt):
        btn = self.ids["Overhead_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Arnold_Press(self, dt):
        btn = self.ids["Arnold_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Lateral_Raises(self, dt):
        btn = self.ids["Lateral_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Front_Raises(self, dt):
        btn = self.ids["Front_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Rear_Delt_Flyes(self, dt):
        btn = self.ids["Rear_Delt_Flyes"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Face_Pulls(self, dt):
        btn = self.ids["Face_Pulls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Push_Press(self, dt):
        btn = self.ids["Push_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Upright_Rows(self, dt):
        btn = self.ids["Upright_Rows"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Cable_Lateral_Raises(self, dt):
        btn = self.ids["Cable_Lateral_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Rack_Pulls(self, dt):
        btn = self.ids["Rack_Pulls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class BicepWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Barbell_Curl, 0)
            Clock.schedule_once(self.Dumbell_Curl, 0)
            Clock.schedule_once(self.Hammer_Curl, 0)
            Clock.schedule_once(self.Preacher_Curl, 0)
            Clock.schedule_once(self.Concentration_Curl, 0)
            Clock.schedule_once(self.Incline_Dumbell_Curl, 0)
            Clock.schedule_once(self.Cable_Curl, 0)
            Clock.schedule_once(self.EzBar_Curl, 0)
            Clock.schedule_once(self.Chin_Up, 0)
            Clock.schedule_once(self.Zottman_Curl, 0)
            Clock.schedule_once(self.back_btn, 0)


    def Barbell_Curl(self, dt):
        btn = self.ids["Barbell_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Dumbell_Curl(self, dt):
        btn = self.ids["Dumbell_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Hammer_Curl(self, dt):
        btn = self.ids["Hammer_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Preacher_Curl(self, dt):
        btn = self.ids["Preacher_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Concentration_Curl(self, dt):
        btn = self.ids["Concentration_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Incline_Dumbell_Curl(self, dt):
        btn = self.ids["Incline_Dumbell_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Cable_Curl(self, dt):
        btn = self.ids["Cable_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def EzBar_Curl(self, dt):
        btn = self.ids["EzBar_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Chin_Up(self, dt):
        btn = self.ids["Chin_Up"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Zottman_Curl(self, dt):
        btn = self.ids["Zottman_Curl"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class ForearmWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Wrist_Curls, 0)
            Clock.schedule_once(self.Reverse_Wrist_Curls, 0)
            Clock.schedule_once(self.Hammer_Curls, 0)
            Clock.schedule_once(self.Reverse_Curls, 0)
            Clock.schedule_once(self.Farmers_Carry, 0)
            Clock.schedule_once(self.Wrist_Roller, 0)
            Clock.schedule_once(self.Dead_Hangs, 0)
            Clock.schedule_once(self.Plate_Pinch_Hold, 0)
            Clock.schedule_once(self.Towel_Pulls_Up, 0)
            Clock.schedule_once(self.Barbell_Holds, 0)
            Clock.schedule_once(self.back_btn, 0)



    def Wrist_Curls(self, dt):
        btn = self.ids["Wrist_Curls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Reverse_Wrist_Curls(self, dt):
        btn = self.ids["Reverse_Wrist_Curls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Hammer_Curls(self, dt):
        btn = self.ids["Hammer_Curls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Reverse_Curls(self, dt):
        btn = self.ids["Reverse_Curls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Farmers_Carry(self, dt):
        btn = self.ids["Farmers_Carry"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Wrist_Roller(self, dt):
        btn = self.ids["Wrist_Roller"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Dead_Hangs(self, dt):
        btn = self.ids["Dead_Hangs"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Plate_Pinch_Hold(self, dt):
        btn = self.ids["Plate_Pinch_Hold"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Towel_Pulls_Up(self, dt):
        btn = self.ids["Towel_Pulls_Up"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Barbell_Holds(self, dt):
        btn = self.ids["Barbell_Holds"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    
class AbsWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Crunches, 0)
            Clock.schedule_once(self.Sit_Ups, 0)
            Clock.schedule_once(self.Leg_Raises, 0)
            Clock.schedule_once(self.Plank, 0)
            Clock.schedule_once(self.Bycicle_Crunches, 0)
            Clock.schedule_once(self.Russian_Twists, 0)
            Clock.schedule_once(self.Mountain_Climbers, 0)
            Clock.schedule_once(self.V_Ups, 0)
            Clock.schedule_once(self.Flutter_Kicks, 0)
            Clock.schedule_once(self.Toe_Touches, 0)
            Clock.schedule_once(self.back_btn, 0)




    def Crunches(self, dt):
        btn = self.ids["Crunches"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Sit_Ups(self, dt):
        btn = self.ids["Sit_Ups"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Leg_Raises(self, dt):
        btn = self.ids["Leg_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Plank(self, dt):
        btn = self.ids["Plank"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Bycicle_Crunches(self, dt):
        btn = self.ids["Bycicle_Crunches"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Russian_Twists(self, dt):
        btn = self.ids["Russian_Twists"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Mountain_Climbers(self, dt):
        btn = self.ids["Mountain_Climbers"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def V_Ups(self, dt):
        btn = self.ids["V_Ups"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Flutter_Kicks(self, dt):
        btn = self.ids["Flutter_Kicks"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Toe_Touches(self, dt):
        btn = self.ids["Toe_Touches"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class QuadsWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Squats, 0)
            Clock.schedule_once(self.Front_Squats, 0)
            Clock.schedule_once(self.Leg_Press, 0)
            Clock.schedule_once(self.Lunges, 0)
            Clock.schedule_once(self.Bulgarian_Split_Squats, 0)
            Clock.schedule_once(self.Step_Ups, 0)
            Clock.schedule_once(self.Leg_Extensions, 0)
            Clock.schedule_once(self.Hack_Squats, 0)
            Clock.schedule_once(self.Goblet_Squats, 0)
            Clock.schedule_once(self.Sissy_Squats, 0)
            Clock.schedule_once(self.back_btn, 0)

    def Squats(self, dt):
        btn = self.ids["Squats"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Front_Squats(self, dt):
        btn = self.ids["Front_Squats"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Leg_Press(self, dt):
        btn = self.ids["Leg_Press"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Lunges(self, dt):
        btn = self.ids["Lunges"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Bulgarian_Split_Squats(self, dt):
        btn = self.ids["Bulgarian_Split_Squats"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Step_Ups(self, dt):
        btn = self.ids["Step_Ups"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Leg_Extensions(self, dt):
        btn = self.ids["Leg_Extensions"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Hack_Squats(self, dt):
        btn = self.ids["Hack_Squats"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Goblet_Squats(self, dt):
        btn = self.ids["Goblet_Squats"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Sissy_Squats(self, dt):
        btn = self.ids["Sissy_Squats"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class HamstringWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Romanian_Deadlifts, 0)
            Clock.schedule_once(self.Stiff_Leg_Deadlift, 0)
            Clock.schedule_once(self.Conventional_Deadlifts, 0)
            Clock.schedule_once(self.Good_Mornings, 0)
            Clock.schedule_once(self.Lying_Leg_Curls, 0)
            Clock.schedule_once(self.Seated_Leg_Curls_Machine, 0)
            Clock.schedule_once(self.Nordic_Hamstring_Curls, 0)
            Clock.schedule_once(self.Glute_Ham_Raises, 0)
            Clock.schedule_once(self.Cable_Leg_Curls, 0)
            Clock.schedule_once(self.Kettlebell_Swings, 0)
            Clock.schedule_once(self.back_btn, 0)


    def Romanian_Deadlifts(self, dt):
        btn = self.ids["Romanian_Deadlifts"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Stiff_Leg_Deadlift(self, dt):
        btn = self.ids["Stiff_Leg_Deadlift"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Conventional_Deadlifts(self, dt):
        btn = self.ids["Conventional_Deadlifts"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Good_Mornings(self, dt):
        btn = self.ids["Good_Mornings"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Lying_Leg_Curls(self, dt):
        btn = self.ids["Lying_Leg_Curls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Seated_Leg_Curls_Machine(self, dt):
        btn = self.ids["Seated_Leg_Curls_Machine"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Nordic_Hamstring_Curls(self, dt):
        btn = self.ids["Nordic_Hamstring_Curls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Glute_Ham_Raises(self, dt):
        btn = self.ids["Glute_Ham_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Cable_Leg_Curls(self, dt):
        btn = self.ids["Cable_Leg_Curls"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Kettlebell_Swings(self, dt):
        btn = self.ids["Kettlebell_Swings"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class CalvesWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Standing_Calf_Raises, 0)
            Clock.schedule_once(self.Seated_Curl_Raises, 0)
            Clock.schedule_once(self.Donkey_Calf_Raises, 0)
            Clock.schedule_once(self.Single_Leg_Calf_Raises, 0)
            Clock.schedule_once(self.Leg_Press_Calf_Raises, 0)
            Clock.schedule_once(self.Smith_Machine_Calf_Raises, 0)
            Clock.schedule_once(self.Farmers_Walk_On_Toes, 0)
            Clock.schedule_once(self.Jump_Rope, 0)
            Clock.schedule_once(self.Box_Jumps, 0)
            Clock.schedule_once(self.TipToe_Walks, 0)
            Clock.schedule_once(self.back_btn, 0)

    def Standing_Calf_Raises(self, dt):
        btn = self.ids["Standing_Calf_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Seated_Curl_Raises(self, dt):
        btn = self.ids["Seated_Curl_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Donkey_Calf_Raises(self, dt):
        btn = self.ids["Donkey_Calf_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Single_Leg_Calf_Raises(self, dt):
        btn = self.ids["Single_Leg_Calf_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Leg_Press_Calf_Raises(self, dt):
        btn = self.ids["Leg_Press_Calf_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Smith_Machine_Calf_Raises(self, dt):
        btn = self.ids["Smith_Machine_Calf_Raises"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Farmers_Walk_On_Toes(self, dt):
        btn = self.ids["Farmers_Walk_On_Toes"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Jump_Rope(self, dt):
        btn = self.ids["Jump_Rope"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Box_Jumps(self, dt):
        btn = self.ids["Box_Jumps"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def TipToe_Walks(self, dt):
        btn = self.ids["TipToe_Walks"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

class BackWorkout(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.Barbell_Shrug, 0)
            Clock.schedule_once(self.Bent_Over_Row, 0)
            Clock.schedule_once(self.Cable_Row, 0)
            Clock.schedule_once(self.Deadlift, 0)
            Clock.schedule_once(self.Dumbell_Row, 0)
            Clock.schedule_once(self.Face_Pull, 0)
            Clock.schedule_once(self.Lat_Pulldown, 0)
            Clock.schedule_once(self.Pull_Up, 0)
            Clock.schedule_once(self.Inverted_Row, 0)
            Clock.schedule_once(self.Rack_Pull, 0)
            Clock.schedule_once(self.Seated_Row, 0)
            Clock.schedule_once(self.Wide_Grip_Pull_Up, 0)
            Clock.schedule_once(self.back_btn, 0)
    
    def Barbell_Shrug(self, dt):
        btn = self.ids["Barbell_Shrug"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Bent_Over_Row(self, dt):
        btn = self.ids["Bent_Over_Row"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Cable_Row(self, dt):
        btn = self.ids["Cable_Row"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Deadlift(self, dt):
        btn = self.ids["Deadlift"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Dumbell_Row(self, dt):
        btn = self.ids["Dumbell_Row"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Face_Pull(self, dt):
        btn = self.ids["Face_Pull"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Lat_Pulldown(self, dt):
        btn = self.ids["Lat_Pulldown"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Pull_Up(self, dt):
        btn = self.ids["Pull_Up"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Rack_Pull(self, dt):
        btn = self.ids["Rack_Pull"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Seated_Row(self, dt):
        btn = self.ids["Seated_Row"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Inverted_Row(self, dt):
        btn = self.ids["Inverted_Row"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def Wide_Grip_Pull_Up(self, dt):
        btn = self.ids["Wide_Grip_Pull_Up"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)


class change_font_screen(Screen):
    def on_enter(self):
        if data["white_mode"] is True:
            Clock.schedule_once(self.f11l, 0)
            Clock.schedule_once(self.f12l, 0)
            Clock.schedule_once(self.f13l, 0)
            Clock.schedule_once(self.f14l, 0)
            Clock.schedule_once(self.f15l, 0)
            Clock.schedule_once(self.f16l, 0)
            Clock.schedule_once(self.f17l, 0)
            Clock.schedule_once(self.f18l, 0)
            Clock.schedule_once(self.f19l, 0)
            Clock.schedule_once(self.f20l, 0)
            Clock.schedule_once(self.f20l, 0)
            Clock.schedule_once(self.f21l, 0)
            Clock.schedule_once(self.f22l, 0)
            Clock.schedule_once(self.f23l, 0)
            Clock.schedule_once(self.f24l, 0)
            Clock.schedule_once(self.f24l, 0)
            Clock.schedule_once(self.f25l, 0)
            Clock.schedule_once(self.f26l, 0)
            Clock.schedule_once(self.f27l, 0)
            Clock.schedule_once(self.f28l, 0)
            Clock.schedule_once(self.f29l, 0)
            Clock.schedule_once(self.f30l, 0)
            Clock.schedule_once(self.f40l, 0)
            Clock.schedule_once(self.f50l, 0)
            Clock.schedule_once(self.f60l, 0)
            Clock.schedule_once(self.f70l, 0)
            Clock.schedule_once(self.f80l, 0)
            Clock.schedule_once(self.f90l, 0)
            Clock.schedule_once(self.back_btn, 0)
        if data["white_mode"] is False:
            Clock.schedule_once(self.f11b, 0)
            Clock.schedule_once(self.f12b, 0)
            Clock.schedule_once(self.f13b, 0)
            Clock.schedule_once(self.f14b, 0)
            Clock.schedule_once(self.f15b, 0)
            Clock.schedule_once(self.f16b, 0)
            Clock.schedule_once(self.f17b, 0)
            Clock.schedule_once(self.f18b, 0)
            Clock.schedule_once(self.f19b, 0)
            Clock.schedule_once(self.f20b, 0)
            Clock.schedule_once(self.f20b, 0)
            Clock.schedule_once(self.f21b, 0)
            Clock.schedule_once(self.f22b, 0)
            Clock.schedule_once(self.f23b, 0)
            Clock.schedule_once(self.f24b, 0)
            Clock.schedule_once(self.f24b, 0)
            Clock.schedule_once(self.f25b, 0)
            Clock.schedule_once(self.f26b, 0)
            Clock.schedule_once(self.f27b, 0)
            Clock.schedule_once(self.f28b, 0)
            Clock.schedule_once(self.f29b, 0)
            Clock.schedule_once(self.f30b, 0)
            Clock.schedule_once(self.f40b, 0)
            Clock.schedule_once(self.f50b, 0)
            Clock.schedule_once(self.f60b, 0)
            Clock.schedule_once(self.f70b, 0)
            Clock.schedule_once(self.f80b, 0)
            Clock.schedule_once(self.f90b, 0)
            Clock.schedule_once(self.back_btnb, 0)


    def f11l(self, dt):
        btn = self.ids["f11"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f12l(self, dt):
        btn = self.ids["f12"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f13l(self, dt):
        btn = self.ids["f13"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f14l(self, dt):
        btn = self.ids["f14"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f15l(self, dt):
        btn = self.ids["f15"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f16l(self, dt):
        btn = self.ids["f16"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f17l(self, dt):
        btn = self.ids["f17"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f18l(self, dt):
        btn = self.ids["f18"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f19l(self, dt):
        btn = self.ids["f19"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f20l(self, dt):
        btn = self.ids["f20"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f21l(self, dt):
        btn = self.ids["f21"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f22l(self, dt):
        btn = self.ids["f22"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f23l(self, dt):
        btn = self.ids["f23"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f24l(self, dt):
        btn = self.ids["f24"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f25l(self, dt):
        btn = self.ids["f25"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f26l(self, dt):
        btn = self.ids["f26"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f27l(self, dt):
        btn = self.ids["f27"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f28l(self, dt):
        btn = self.ids["f28"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f29l(self, dt):
        btn = self.ids["f29"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f30l(self, dt):
        btn = self.ids["f30"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f40l(self, dt):
        btn = self.ids["f40"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f50l(self, dt):
        btn = self.ids["f50"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f60l(self, dt):
        btn = self.ids["f60"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f70l(self, dt):
        btn = self.ids["f70"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f80l(self, dt):
        btn = self.ids["f80"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def f90l(self, dt):
        btn = self.ids["f90"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)
    def back_btn(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (1, 1, 1, 1)
        btn.background_normal = ''
        btn.color = (0, 0, 0, 1)

    













    def f11b(self, dt):
        btn = self.ids["f11"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f12b(self, dt):
        btn = self.ids["f12"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f13b(self, dt):
        btn = self.ids["f13"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f14b(self, dt):
        btn = self.ids["f14"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f15b(self, dt):
        btn = self.ids["f15"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f16b(self, dt):
        btn = self.ids["f16"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f17b(self, dt):
        btn = self.ids["f17"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f18b(self, dt):
        btn = self.ids["f18"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f19b(self, dt):
        btn = self.ids["f19"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f20b(self, dt):
        btn = self.ids["f20"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f21b(self, dt):
        btn = self.ids["f21"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f22b(self, dt):
        btn = self.ids["f22"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f23b(self, dt):
        btn = self.ids["f23"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f24b(self, dt):
        btn = self.ids["f24"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f25b(self, dt):
        btn = self.ids["f25"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f26b(self, dt):
        btn = self.ids["f26"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f27b(self, dt):
        btn = self.ids["f27"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f28b(self, dt):
        btn = self.ids["f28"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f29b(self, dt):
        btn = self.ids["f29"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f30b(self, dt):
        btn = self.ids["f30"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f40b(self, dt):
        btn = self.ids["f40"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f50b(self, dt):
        btn = self.ids["f50"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f60b(self, dt):
        btn = self.ids["f60"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f70b(self, dt):
        btn = self.ids["f70"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f80b(self, dt):
        btn = self.ids["f80"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)
    def f90b(self, dt):
        btn = self.ids["f90"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)

    def back_btnb(self, dt):
        btn = self.ids["back_btn"]
        btn.background_color = (0, 0, 0, 1)
        btn.background_normal = ''
        btn.color = (1, 1, 1, 1)



    def f11(self):
        data["font_size"] = 11

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f12(self):
        data["font_size"] = 12

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f13(self):
        data["font_size"] = 13

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f14(self):
        data["font_size"] = 14

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f15(self):
        data["font_size"] = 15

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f16(self):
        data["font_size"] = 16

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f17(self):
        data["font_size"] = 17

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f18(self):
        data["font_size"] = 18

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f19(self):
        data["font_size"] = 19

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f20(self):
        data["font_size"] = 20

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f21(self):
        data["font_size"] = 21

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f22(self):
        data["font_size"] = 22

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f23(self):
        data["font_size"] = 23

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f24(self):
        data["font_size"] = 24

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f25(self):
        data["font_size"] = 25

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f26(self):
        data["font_size"] = 26

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f27(self):
        data["font_size"] = 27

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f28(self):
        data["font_size"] = 28

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f29(self):
        data["font_size"] = 29

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f30(self):
        data["font_size"] = 30

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f40(self):
        data["font_size"] = 40

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f50(self):
        data["font_size"] = 50

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f60(self):
        data["font_size"] = 60

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f70(self):
        data["font_size"] = 70

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f80(self):
        data["font_size"] = 80

        with open("logs.json", "w") as file:
                json.dump(data, file)
    def f90(self):
        data["font_size"] = 90

        with open("logs.json", "w") as file:
                json.dump(data, file)





class MyApp(App):
    def build(self):
        return ScreenManagerApp()

class ScreenManagerApp(ScreenManager):
    pass

if __name__ == '__main__':
    MyApp().run()
