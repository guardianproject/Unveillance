"""
	STATIC PATHS:
	In this section, fill in all of these values with whatever makes sense to you.
"""
public_user = "USER_NAME"
conf = "/path/to/your/conf/"
assets_root = "/path/to/your/assets/"
gnupg_home = "/path/to/your/users/.gnupg"
forms_root = "/path/to/your/forms/"
scripts_home = {
	"python" : '/path/to/Unveillance/scripts/py/'
}
elasticsearch_home = "/path/to/where/you/put/elasticsearch/"
secret_key_path = '/path/to/your/secret/key/for/gnupg/key.asc'
gnugp_pwd = "/path/to/your/gpg/password"

file_salt = "WHAT WILL YOUR SALT BE?"
anon_salt = "16 bytes of goodness"	# 16
anon_iv = "16 bytes of goodness"	# 16

j3m = {
	"root" : "/path/to/where/you/have/packages/j3m/"
}

"""
	REPOSITORY SYNC:
	This array can be populated with whatever repositories you currently host.  
	So far, we support 'globaleaks' and 'google_drive'.  You DEFINITELY SHOULD LEAVE 'import' in there; it monitors your local drive for imported media.
	
	All private keys should be put in your conf folder so we can reference them.
"""
sync = [
	'import',
	'globaleaks'
]

drive = {
	"client_secrets" : "%sclient_secrets.json" % conf,
	"p12" : "%sGOOGLE_DRIVE-privatekey.p12" % conf,
	"asset_root" : "GOOGLE DRIVE ID OF FOLDER WHERE YOUR SUBMISSIONS ARE HELD",
	"absorbed_flag" : "absorbedByInformaCam",
	"asset_id" : "google service account email",
	"absorbed_log" : "%sabsorbedByInformaCam_gd.tx" % assets_root,
}

globaleaks = {
	"asset_root" : "/var/globaleaks/files/submission/",
	"host" : "wheres-your-gl-server.com",
	"user" : "user",
	"context_gus" : "GL CONTEXT GUS",
	"identity_file" : "%sgltest1.pem" % conf,
	"absorbed_log" : "%sabsorbedByInformaCam_gl.txt" % assets_root,
	"absorbed_flag" : "absorbedByInformaCam",
	"public_url" : "http://WHATEVER_PUBLIC_URL.onion"
}

import_directory = {
	"asset_root" : "/where/will/you/put/imported/media/",
	"absorbed_log" : "%sabsorbedByInformaCam_import.txt" % assets_root
}

"""
	YOUR ICTD INFO:
	Whenever a user visits your public site, you will serve up this information in
	an ICTD file, on-the-fly.
	
	Below is an example of how to register your custom forms for users to use in-app.
	Those files must be in your forms_root.
"""
organization_fingerprint = "FULL FINGERPRINT PLEASE"
organization_name = "What do we call you?"
organization_details = "What else do you have to say?"
public_key_path = '/where/is/your/public/key.asc'

forms = [
	'%siWitness_free_text.xml' % forms_root,
	'%siWitness_free_audio.xml' % forms_root,
	'%siWitness_v_1_0.xml' % forms_root
]

"""
	If you don't support any of these repositories, remove their entries
"""
repositories = [
	{
		'source': 'google_drive',
		'asset_id': drive['asset_root'],
		'asset_root': 'https://drive.google.com'
	},
	{
		'source': 'globaleaks',
		'asset_id': globaleaks['context_gus'],
		'asset_root': globaleaks['public_url']
	}

]

"""
	NOTHING ELSE TO CHANGE!  Don't worry about the rest of these values!
"""
log_root = assets_root
sync_sleep = 2	# minutes
validity_buffer = {
	'location' : (5 * 60 * 1000), # 5 minutes
	'stale_data' : ((((60 * 1000) * 60) * 24) * 30) # 30 days
}

submissions_dump = "%ssubmissions/" % assets_root

api = {
	'port' : 8080,
	'num_processes' : 20
}

invalidate = {
	'codes' : {
		'asset_non_existent': 801,
		'source_invalid_pgp_key' : 902,
		'source_invalid_public_credentials' : 903,
		'source_missing_pgp_key' : 905,
		'submission_invalid_image' : 900,
		'submission_invalid_video' : 901,
		'submission_invalid_j3m' : 904,
		'submission_undefined' : 906,
		'access_denied' : 800,
		'unindexible' : 700,
		'j3m_not_verified' : 907
	},
	'reasons' : {
		'asset_non_existent': "The requested asset does not exist",
		'source_invalid_pgp_key' : "The pgp key is invalid or corrupted",
		'source_missing_pgp_key' : "This source has no PGP key in the keyring",
		'source_invalid_public_credentials' : "One or more of the public credentials files are invalid or corrupted",
		'submission_invalid_image' : "The image is invalid or corrupted",
		'submission_invalid_video' : "The video is invalid or corrupted",
		'submission_invalid_j3m' : "The j3m for this submission is invalid or missing",
		'submission_undefined' : "The derivative has no defined submission",
		'access_denied' : "The user is attempting to access an asset beyond its permissions.",
		'unindexible' : "This asset could not be indexed by elasticsearch",
		'j3m_not_verified' : "This J3M is not verified"
	}
}

public = {
	"organizationName" : organization_name,
	"organizationDetails" : organization_details,
	"organizationFingerprint" : organization_fingerprint,
	"repositories": repositories,
	"publicKey": public_key_path,
	"forms": forms
}

mime_types = {
        'j3m': "text/plain",
        'zip' : "application/zip",
        'image' : "image/jpeg",
        'video' : "video/x-matroska",
        'wildcard' : "application/octet-stream",
        'pgp' : "application/pgp",
        'gzip' : "application/x-gzip",
        '3gp' : 'video/3gpp'
}

mime_type_map = {
        'text/plain': "json",
        'application/zip': "zip",
        'image/jpeg': "jpg",
        'video/x-matroska': "mkv",
        'application/octet-stream': 'wildcard',
        'application/pgp' : 'pgp',
        'application/x-gzip' : 'gzip',
        'video/3gpp' : '3gp'
}
