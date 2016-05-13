import maya.cmds as cmds
import Scripts.General_Maya_Util

#---------------------------------------------------------------------------
def aw_hub_turn_On_All_Panel_HUDs():
	panelList = cmds.getPanel(type="modelPanel")
	for currentPanel in panelList:   
		cmds.modelEditor(currentPanel,e=True,hud=True)
#---------------------------------------------------------------------------
def aw_hub_Return_HUD_Slider_Value( slider_name ):
	return cmds.hudSlider(slider_name, q=True, v=True)
#---------------------------------------------------------------------------
def aw_hub_Turn_Off():
	aw_hub_clear_hub()
	visibility_option = Scripts.General_Maya_Util.OptionVar("aw_model_editor_headsup_display_controls_Visibility", 0)
	visibility_option.value = 0
#---------------------------------------------------------------------------
def aw_hub_clear_hub():
	""""""
	HUDCount = 26
	for i in range(1,HUDCount):
		cmds.headsUpDisplay(removePosition=(5,i))

#---------------------------------------------------------------------------
def aw_hub_view_Display_Controls():
	def toggle_selection_hilighting():
		cmds.modelEditor(cmds.getPanel( withFocus=True),edit=True,sel=not cmds.modelEditor(cmds.getPanel( withFocus=True),q=True,sel=True))
	# cmds.headsUpDisplay("HUDViewAxis",edit=True ,vis=0)
	maxGridSize = Scripts.General_Maya_Util.OptionVar("aw_model_editor_headsup_display_controls_maxGridSize", 5000)
	gridSize = cmds.grid(q=True,size=True)
	cmds.getPanel( withFocus=True)
	aw_hub_clear_hub()
	cmds.hudButton("aw_HUD_Minimize_Buttons", section=5, block=3, visible=True, label="- Minimize -", buttonWidth=100, buttonShape="roundRectangle", releaseCommand=aw_hub_Main_Controls)
	cmds.hudButton("aw_HUD_Selection_HiLighting", section=5, block=2, visible=True, label="Tog Sel Hi-Lit", buttonWidth=100, buttonShape="roundRectangle", releaseCommand=toggle_selection_hilighting)
	#cmds.hudSlider("aw_HUD_Grid_Slider",section=5, block=2, visible=True, label="        Grid Size:",
	#						value = gridSize,
	#						t = "float",
	#						minValue = 5,
	#						maxValue = maxGridSize.value,
	#						labelWidth = 115,
	#						valueWidth = 100,
	#						sliderLength = 400,
	#						sliderIncrement = 5,
	#						pressCommand = lambda :cmds.undoInfo(stateWithoutFlush=False),
	#						dragCommand  = lambda name="aw_HUD_Grid_Slider":cmds.grid(size=aw_hub_Return_HUD_Slider_Value(name)),
	#						releaseCommand = lambda :cmds.undoInfo(stateWithoutFlush=True))
	cmds.hudButton("aw_HUD_KillButtons", section=5, block=1, visible=True, label="Close", buttonWidth=100, buttonShape="roundRectangle", releaseCommand=aw_hub_Turn_Off)
#---------------------------------------------------------------------------
def aw_hub_Main_Controls():
	aw_hub_clear_hub()
	cmds.hudButton("aw_HUD_ViewDispButtons", block=2, buttonShape="roundRectangle", buttonWidth=110, label=">  View Display", releaseCommand=aw_hub_view_Display_Controls, section=5, visible=True)
	#cmds.hudButton("aw_HUD_AnimDispButtons", block=3, buttonShape="roundRectangle", buttonWidth=110, label=">  Anim Display", releaseCommand="bt_animDisplayControlHUD", section=5, visible=True)
	#cmds.hudButton("aw_HUD_PolyDispButton" , block=2, buttonShape="roundRectangle", buttonWidth=110, label=">  Poly Display", releaseCommand="bt_polyDisplayControlHUD", section=5, visible=True)
	cmds.hudButton("aw_HUD_KillButtons" , block=1, buttonShape="roundRectangle", buttonWidth=110, label="Close", releaseCommand=aw_hub_Turn_Off, section=5, visible=True)
#---------------------------------------------------------------------------
def AW_HUB_Master_Control():
	""""""
	#aw_hub_check_Ctr1_Hotkey()
	aw_hub_turn_On_All_Panel_HUDs()
	visibility_option = Scripts.General_Maya_Util.OptionVar("aw_model_editor_headsup_display_controls_Visibility", 0)
	if not visibility_option.value:
		visibility_option.value = 1
	aw_hub_clear_hub()
	aw_hub_Main_Controls()

		#Scripts.UICls.Controls.HudButton
		#cmds.hudButton("aw_HUD_ViewDispButtons", block=2, buttonShape="roundRectangle", buttonWidth=110, label=">  View Display", releaseCommand="bt_viewDisplayControlHUD", section=5, visible=True)
		#cmds.hudButton("aw_HUD_AnimDispButtons", block=3, buttonShape="roundRectangle", buttonWidth=110, label=">  Anim Display", releaseCommand="bt_animDisplayControlHUD", section=5, visible=True)
		#cmds.hudButton("aw_HUD_PolyDispButton" , block=2, buttonShape="roundRectangle", buttonWidth=110, label=">  Poly Display", releaseCommand="bt_polyDisplayControlHUD", section=5, visible=True)
		#cmds.hudButton("aw_HUD_KillButtons" , block=1, buttonShape="roundRectangle", buttonWidth=110, label="Close", releaseCommand=aw_hub_Turn_Off, section=5, visible=True)

