extends PanelContainer
class_name ControlPanel

signal play_pause_toggled
signal speed_selected(multiplier: float)
signal save_requested
signal load_requested

@onready var play_pause_button: Button = $MarginContainer/VBoxContainer/PlayPauseButton
@onready var speed_option: OptionButton = $MarginContainer/VBoxContainer/SpeedOption

func _ready() -> void:
	speed_option.clear()
	for value in [0.5, 1.0, 2.0, 4.0]:
		speed_option.add_item("%.1fx" % value)
	speed_option.select(1)

func set_playing(is_playing: bool) -> void:
	play_pause_button.text = "Pause" if is_playing else "Play"

func _on_play_pause_button_pressed() -> void:
	emit_signal("play_pause_toggled")

func _on_speed_option_item_selected(index: int) -> void:
	var options := [0.5, 1.0, 2.0, 4.0]
	emit_signal("speed_selected", options[index])

func _on_save_button_pressed() -> void:
	emit_signal("save_requested")

func _on_load_button_pressed() -> void:
	emit_signal("load_requested")
