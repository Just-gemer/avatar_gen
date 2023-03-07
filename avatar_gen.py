import os, struct, json, zlib
print('AVATAR-GENERATOR BY Just gemer')
ava_id = str(input('avatar id (ex. 0717): '))
descname = 'desc.tpl'
path = 'world/avatars/'+ava_id+'/'
avatarname = 'avatar.png'
try:
    os.mkdir('output')
except:
    pass
os.mkdir('output/'+ava_id)
actor = open('output/' + ava_id + '/' + ava_id + '.act.ckd', 'wb')
actor.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00')
actor.write(struct.pack('>I', len(descname))+descname.encode())
actor.write(struct.pack('>I', len(path))+path.encode()+struct.pack("<I",zlib.crc32(descname.encode())))
actor.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x72\xB6\x1F\xC5\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')
actor.write(struct.pack('>I', len(avatarname))+avatarname.encode())
actor.write(struct.pack('>I', len(path))+path.encode()+struct.pack("<I",zlib.crc32(avatarname.encode())))
actor.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0A\x61\x76\x61\x74\x61\x72\x2E\x61\x74\x6C\x00\x00\x00\x0F\x77\x6F\x72\x6C\x64\x2F\x75\x69\x2F\x61\x74\x6C\x61\x73\x2F\x0A\x6F\x64\x68\x00\x00\x00\x00\x00\x00\x00\x09\x61\x6C\x70\x68\x61\x2E\x6D\x73\x68\x00\x00\x00\x1B\x77\x6F\x72\x6C\x64\x2F\x75\x69\x2F\x6D\x61\x74\x65\x72\x69\x61\x6C\x73\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x74\x62\xE0\x51\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x17\x59\xE2\x9D')
actor.close()
if ava_id == '0'+ava_id[1]+ava_id[2]+ava_id[3]:
    ava_id_clear=ava_id.replace('0','')
    desc = open('output/' + ava_id + '/desc.tpl.ckd', 'w')
    desc.write('''{
	"__class": "Actor_Template",
	"WIP": 0,
	"LOWUPDATE": 0,
	"UPDATE_LAYER": 0,
	"PROCEDURAL": 0,
	"STARTPAUSED": 0,
	"FORCEISENVIRONMENT": 0,
	"COMPONENTS": [
		{
			"__class": "MaterialGraphicComponent_Template",
			"patchLevel": 0,
			"patchHLevel": 2,
			"patchVLevel": 2,
			"visualAABB": {
				"__class": "AABB",
				"MIN": [
					0,
					0
				],
				"MAX": [
					0,
					0
				]
			},
			"renderintarget": 0,
			"posOffset": [
				0,
				0
			],
			"angleOffset": 0,
			"blendmode": 2,
			"materialtype": 0,
			"selfIllumColor": [
				0,
				0,
				0,
				0
			],
			"disableLight": 0,
			"forceDisableLight": 0,
			"useShadow": 0,
			"useRootBone": 0,
			"shadowSize": [
				1.8,
				0.3
			],
			"shadowMaterial": {
				"__class": "GFXMaterialSerializable",
				"textureSet": {
					"__class": "GFXMaterialTexturePathSet",
					"diffuse": "",
					"back_light": "",
					"normal": "",
					"separateAlpha": "",
					"diffuse_2": "",
					"back_light_2": "",
					"anim_impostor": "",
					"diffuse_3": "",
					"diffuse_4": ""
				},
				"ATL_Channel": 0,
				"ATL_Path": "",
				"shaderPath": "",
				"materialParams": {
					"__class": "GFXMaterialSerializableParam",
					"Reflector_factor": 0
				},
				"outlinedMaskParams": {
					"__class": "OutlinedMaskMaterialParams",
					"maskColor": [
						0,
						0,
						0,
						0
					],
					"outlineColor": [
						0,
						0,
						0,
						0
					],
					"thickness": 1
				},
				"alphaTest": 4294967295,
				"alphaRef": 4294967295
			},
			"shadowAttenuation": 1,
			"shadowDist": 4,
			"shadowOffsetPos": [
				0,
				0,
				0
			],
			"angleLimit": 0,
			"material": {
				"__class": "GFXMaterialSerializable",
				"textureSet": {
					"__class": "GFXMaterialTexturePathSet",
					"diffuse": "",
					"back_light": "",
					"normal": "",
					"separateAlpha": "",
					"diffuse_2": "",
					"back_light_2": "",
					"anim_impostor": "",
					"diffuse_3": "",
					"diffuse_4": ""
				},
				"ATL_Channel": 0,
				"ATL_Path": "",
				"shaderPath": "",
				"materialParams": {
					"__class": "GFXMaterialSerializableParam",
					"Reflector_factor": 0
				},
				"outlinedMaskParams": {
					"__class": "OutlinedMaskMaterialParams",
					"maskColor": [
						0,
						0,
						0,
						0
					],
					"outlineColor": [
						0,
						0,
						0,
						0
					],
					"thickness": 1
				},
				"alphaTest": 4294967295,
				"alphaRef": 4294967295
			},
			"defaultColor": [
				1,
				1,
				1,
				1
			],
			"zOffset": 0
		},
		{
			"__class": "JD_AvatarDescTemplate",
			"JdVersion": 2022,
			"RelativeSongName": "",
			"RelativeQuestID": "",
			"RelativeWDFBossName": "",
			"RelativeWDFTournamentName": "",
			"RelativeJDRank": "",
			"RelativeGameModeName": "",
			"SoundFamily": "AVTR_Common_Boy_Child",
			"Status": 1,
			"UnlockType": 1,
			"MojoPrice": 0,
			"WdfLevel": 1,
			"CountInProgression": 1,
			"ActorPath": "world/avatars/'''+ava_id+'''/'''+ava_id+'''.act",
			"PhoneImage": "world/avatars/'''+ava_id+'''/avatar_phone.png",
			"AvatarId": '''+ava_id_clear+''',
			"UsedAsCoach_MapName": "",
			"UsedAsCoach_CoachId": 0,
			"specialEffect": 0,
			"mainAvatarId": 65535
		}
	]
}''')
    desc.close()
    print('done')
else:
    desc = open('output/' + ava_id + '/desc.tpl.ckd', 'w')
    desc.write('''{
	"__class": "Actor_Template",
	"WIP": 0,
	"LOWUPDATE": 0,
	"UPDATE_LAYER": 0,
	"PROCEDURAL": 0,
	"STARTPAUSED": 0,
	"FORCEISENVIRONMENT": 0,
	"COMPONENTS": [
		{
			"__class": "MaterialGraphicComponent_Template",
			"patchLevel": 0,
			"patchHLevel": 2,
			"patchVLevel": 2,
			"visualAABB": {
				"__class": "AABB",
				"MIN": [
					0,
					0
				],
				"MAX": [
					0,
					0
				]
			},
			"renderintarget": 0,
			"posOffset": [
				0,
				0
			],
			"angleOffset": 0,
			"blendmode": 2,
			"materialtype": 0,
			"selfIllumColor": [
				0,
				0,
				0,
				0
			],
			"disableLight": 0,
			"forceDisableLight": 0,
			"useShadow": 0,
			"useRootBone": 0,
			"shadowSize": [
				1.8,
				0.3
			],
			"shadowMaterial": {
				"__class": "GFXMaterialSerializable",
				"textureSet": {
					"__class": "GFXMaterialTexturePathSet",
					"diffuse": "",
					"back_light": "",
					"normal": "",
					"separateAlpha": "",
					"diffuse_2": "",
					"back_light_2": "",
					"anim_impostor": "",
					"diffuse_3": "",
					"diffuse_4": ""
				},
				"ATL_Channel": 0,
				"ATL_Path": "",
				"shaderPath": "",
				"materialParams": {
					"__class": "GFXMaterialSerializableParam",
					"Reflector_factor": 0
				},
				"outlinedMaskParams": {
					"__class": "OutlinedMaskMaterialParams",
					"maskColor": [
						0,
						0,
						0,
						0
					],
					"outlineColor": [
						0,
						0,
						0,
						0
					],
					"thickness": 1
				},
				"alphaTest": 4294967295,
				"alphaRef": 4294967295
			},
			"shadowAttenuation": 1,
			"shadowDist": 4,
			"shadowOffsetPos": [
				0,
				0,
				0
			],
			"angleLimit": 0,
			"material": {
				"__class": "GFXMaterialSerializable",
				"textureSet": {
					"__class": "GFXMaterialTexturePathSet",
					"diffuse": "",
					"back_light": "",
					"normal": "",
					"separateAlpha": "",
					"diffuse_2": "",
					"back_light_2": "",
					"anim_impostor": "",
					"diffuse_3": "",
					"diffuse_4": ""
				},
				"ATL_Channel": 0,
				"ATL_Path": "",
				"shaderPath": "",
				"materialParams": {
					"__class": "GFXMaterialSerializableParam",
					"Reflector_factor": 0
				},
				"outlinedMaskParams": {
					"__class": "OutlinedMaskMaterialParams",
					"maskColor": [
						0,
						0,
						0,
						0
					],
					"outlineColor": [
						0,
						0,
						0,
						0
					],
					"thickness": 1
				},
				"alphaTest": 4294967295,
				"alphaRef": 4294967295
			},
			"defaultColor": [
				1,
				1,
				1,
				1
			],
			"zOffset": 0
		},
		{
			"__class": "JD_AvatarDescTemplate",
			"JdVersion": 2022,
			"RelativeSongName": "",
			"RelativeQuestID": "",
			"RelativeWDFBossName": "",
			"RelativeWDFTournamentName": "",
			"RelativeJDRank": "",
			"RelativeGameModeName": "",
			"SoundFamily": "AVTR_Common_Boy_Child",
			"Status": 1,
			"UnlockType": 1,
			"MojoPrice": 0,
			"WdfLevel": 1,
			"CountInProgression": 1,
			"ActorPath": "world/avatars/'''+ava_id+'''/'''+ava_id+'''.act",
			"PhoneImage": "world/avatars/'''+ava_id+'''/avatar_phone.png",
			"AvatarId": '''+ava_id+''',
			"UsedAsCoach_MapName": "",
			"UsedAsCoach_CoachId": 0,
			"specialEffect": 0,
			"mainAvatarId": 65535
		}
	]
}''')
    desc.close()
    print('done')
