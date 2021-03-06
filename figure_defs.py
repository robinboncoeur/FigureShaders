import bpy

sMsg = ""

class matZones():
  def __init__(self, fig):
    self.fig = fig
    self.figMat = {}
    self.listMats()

  def listMats(self):
    if self.fig == 'list_figs':
      self.figMat = {
        'RDNA Antonia': 'Antonia',
        'HiveWire Dawn': 'Dawn',
        'DTG Mariko': 'Mariko',
        'Victoria4': 'V4',
        }

    if self.fig == 'Antonia':
      self.figMat = {
        'brows': 'Skin_Face',
        'lips': 'Skin_Face',
        'skin_HEAD': 'Skin_Face',
        'skin_BODY': 'Skin_Body',
        'skin_ARMS': 'Skin_Arms',
        'skin_LEGS': 'Skin_Legs',
        'nailsFingers': 'Skin_Arms',
        'nailsToes': 'Skin_Legs',
        'mouthinner': 'Mouth',
        'tongue': 'Mouth',
        'teeth': 'Mouth',
        'scleraLeft': 'Eyes_Clr',
        'scleraRight': 'Eyes_Clr',
        'irisLeft': 'Eyes_Clr',
        'irisRight': 'Eyes_Clr',
        'corneaLeft': 'Eyes_Trn',
        'corneaRight': 'Eyes_Trn',
        'pupilLeft': 'Eyes_Clr',
        'pupilRight': 'Eyes_Clr',
        'lacrimals': 'Eyes_Trn',
        'lashes': 'Eyes_Lash',
        'invisible': 'Eyes_Trn',
        'toeCap': 'Eyes_Trn',
        }

    if self.fig == 'V4':
      self.figMat = {
        '1_SkinFace': 'Skin_Face',
        '1_Eyebrow': 'Skin_Face',
        '1_Nostril': 'Skin_Face' ,
        '1_Lip': 'Skin_Face',
        '1_EyeSocket': 'Skin_Body',
        '2_SkinHead': 'Skin_Body',
        '2_SkinNeck': 'Skin_Body',
        '2_SkinTorso': 'Skin_Body',
        '2_Nipple': 'Skin_Body',
        '2_SkinHip': 'Skin_Body',
        '3_SkinArm': 'Skin_Arms',
        '3_SkinForearm': 'Skin_Arms',
        '3_SkinHand': 'Skin_Arms',
        '3_SkinLeg': 'Skin_Legs',
        '3_SkinFoot': 'Skin_Legs',
        '3_Fingernail': 'Skin_Arms',
        '3_Toenail': 'Skin_Legs',
        '4_InnerMouth': 'Mouth',
        '4_Gums': 'Mouth',
        '4_Tongue': 'Mouth',
        '4_Teeth': 'Mouth',
        '5_Sclera': 'Eyes_Clr',
        '5_Iris': 'Eyes_Clr',
        '5_Pupil': 'Eyes_Clr',
        '5_Lacrimal': 'Eyes_Trn',
        '5_Cornea': 'Eyes_Clr',
        '6_Eyelash': 'Eyes_Lash',
        '7_EyeSurface': 'Eyes_Trn',
        '7_Tear': 'Eyes_Trn',
        'Preview': 'Skin',
        }

    if self.fig == 'Dawn':
      self.figMat = {
        '1_Cornea': 'Eyes_Trn',
        '1_Eyes': 'Eyes_Clr',
        '1_Iris': 'Eyes_Clr',
        '1_Lacrimal': 'Eyes_Clr',
        '1_Pupil': 'Eyes_Clr',
        '2_Gums': 'Mouth',
        '2_InnerMouth': 'Mouth',
        '2_Teeth': 'Mouth',
        '2_Tongue': 'Mouth',
        '3A_Arms': 'Skin_Arms',
        '3A_Collars': 'Skin_Arms',
        '3A_Hands': 'Skin_Arms',
        '3B_Feet': 'Skin_Legs',
        '3B_Legs': 'Skin_Legs',
        '3C_Body': 'Skin_Body',
        '3C_Head_Neck': 'Skin_Body',
        '3C_Hip': 'Skin_Body',
        '3_Ears': 'Skin_Face',
        '3_Face': 'Skin_Face',
        '3_Lips': 'Skin_Face',
        '4_Eyelashes': 'Eyes_Lash',
        '4_Eyelashes_Large': 'Eyes_Lash',
        '5_Fingernails': 'Skin_Arms',
        '5_Toenails': 'Skin_Legs',
        'Preview': 'Skin',
        }

    if self.fig == 'Mariko':
      self.figMat = {
        'SkinBody_Front': 'Skin',
        'Nipples': 'Skin',
        'Anus': 'Skin',
        'SkinBody_Back': 'Skin',
        'Toenails': 'Skin',
        'Fingernails': 'Skin',
        'Labia': 'Skin',
        'Clitoris': 'Skin',
        'Vagina': 'Skin',
        'Nipples_Outer': 'Skin',
        'Nipple_Blend_Zone': 'Skin',
        'Pubic_Hair': 'Skin',
        'Skin_Head': 'Skin',
        'Lips': 'Skin',
        'Ear_Canal': 'Skin',
        'Nostrils': 'Skin',
        'Lacrimal': 'TrnEyes',
        'Inside_Mouth': 'Mouth',
        'Gums': 'Mouth',
        'Tongue': 'Mouth',
        'Teeth': 'Mouth',
        'Hair': 'LshEyes',
        'Eyebrows': 'LshEyes',
        'Lashes': 'LshEyes',
        'Lips_Layer_2': 'Skin',
        'EyewhiteOuter': 'ClrEyes',
        'Eyewhite': 'ClrEyes',
        'Pupil': 'ClrEyes',
        'Cornea': 'ClrEyes',
        'Iris': 'ClrEyes',
        'Preview': 'Skin',
        'Skin_Body_Front': 'Skin',
        'Skin_Body_Back': 'Skin',
        'default': 'Skin',
        'Inside_Mouth_Rear': 'Mouth',
        'Inside_Cheek': 'Mouth',
        'Inside_Mouth_Roof': 'Mouth',
        }
