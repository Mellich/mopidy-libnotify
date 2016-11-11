import pykka
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from mopidy import core
import urllib

tmp_icon_uri = "/tmp/mopidy-notify-icon"

class LibNotifyFrontend(pykka.ThreadingActor, core.CoreListener):
	def __init__(self, config, core):
		super(LibNotifyFrontend, self).__init__()
		self.core = core
		self.config = config
		self.artist = "UNKNOWN"
		self.title = "UNKNOWN"
		self.icon = ""
		Notify.init("Mopidy")
	
	def notify(self):
		Hello=Notify.Notification.new(self.artist,self.title, self.icon)
		Hello.show()
	
	def update_artist(self, tl_track):
		self.artist = ""
		for artist in tl_track.track.artists:
			if self.artist != "":
				self.artist = artist_string + " ft. " + artist.name
			else:
				self.artist = artist.name
				
	def download_icon(self, uri):
		if "http://" not in uri:
			return uri
		urllib.urlretrieve(uri, tmp_icon_uri)
		return tmp_icon_uri
	
	def update_icon(self, uris):
		self.icon = ""
		images = self.core.library.get_images(uris)
		try:
			result = images.get() 
			for uri in uris:
				for img in result[uri]:
					self.icon = self.download_icon(img.uri)
					return
		except:
			return
		
		
	def get_uris(self,tl_track):
		uris = []
		uris.append(tl_track.track.uri)
		uris.append(tl_track.track.album.uri)
		for artist in tl_track.track.artists:
			uris.append(artist.uri)
		return uris
						
	def update_title(self, title):
		self.title = title
	
	def track_playback_started(self, tl_track):
		self.update_artist(tl_track)
		self.update_title(tl_track.track.name)
		if self.artist == "":
			splitted = tl_track.track.name.split(" - ")
			if len(splitted) > 1:
				self.artist = splitted[0]
				self.title = splitted[1]
		self.update_icon(self.get_uris(tl_track))
		self.notify()
		
	def track_playback_resumed(self, tl_track, time_position):
		self.notify()
	
	def stream_title_changed(self, title):
		self.update_title(title)		
		self.notify()

    # Your frontend implementation 
