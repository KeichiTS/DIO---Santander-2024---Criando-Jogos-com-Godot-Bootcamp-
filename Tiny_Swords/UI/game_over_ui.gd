class_name GameOverUI
extends CanvasLayer


@onready var timer_label : Label = %Time_Label
@onready var monster_label : Label = %Monster_label

@export var restart_delay : float = 5.0
var restart_cooldown : float

func _ready():
	timer_label.text = GameManager.time_elapsed_string
	monster_label.text = str(GameManager.monsters_defeated_counter)
	restart_cooldown = restart_delay
	
func _process(delta):
	restart_cooldown -= delta
	if restart_cooldown <= 0: 
		restart_game()
		
func restart_game():
	GameManager.reset()
	get_tree().reload_current_scene()
