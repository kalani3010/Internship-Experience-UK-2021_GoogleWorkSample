"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = 'none'
        self._paused_video = 'none'
        self._playlists = {}
        self._playlist_names = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print(f"Here's a list of all available videos:")
        for item in self._video_library.get_all_videos():
            print(f'{item._title} ({item._video_id}) {list(item._tags)}')

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_id_list = list(self._video_library._videos.keys())

        if video_id in video_id_list:
            video_title = self._video_library.get_video(video_id)._title
            if self._current_video == 'none':
                print(f'Playing video:  {self._video_library.get_video(video_id)._title}')
                self._current_video = video_id
            elif self._current_video == video_id or self._current_video != video_id:
                print(f'Stopping video: {self._video_library.get_video(self._current_video)._title}')
                print(f'Playing video:  {self._video_library.get_video(video_id)._title}')
                self._current_video = video_id
        elif video_id not in video_id_list:
            print('Cannot play video: Video does not exist')


    def stop_video(self):
        """Stops the current video."""
        if self._current_video == 'none':
            print('Cannot stop video: No video is currently playing')
        else:
            print(f'Stopping video: {self._video_library.get_video(self._current_video)._title}')
            self._current_video = 'none'

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_id_list = list(self._video_library._videos.keys())

        random_video = random.choice(video_id_list)
        self.play_video(random_video)
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self._current_video == 'none':
            print('Cannot pause video: No video is currently playing')
        elif self._paused_video != 'none':
            if self._paused_video != self._current_video:
                print(f'Pausing video: {self._video_library.get_video(self._current_video)._title}')
                self._paused_video = self._current_video
            else:
                print(f'Video already paused: {self._video_library.get_video(self._paused_video)._title}')
        else:
            print(f'Pausing video: {self._video_library.get_video(self._current_video)._title}')
            self._paused_video = self._current_video
        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._paused_video != self._current_video:
            print('Cannot continue video: Video is not paused')
        elif self._current_video == 'none':
            print('Cannot continue video: No video is currently playing')
        else:
            print(f'Continuing video: {self._video_library.get_video(self._current_video)._title}')
            self._paused_video = 'none'

    def show_playing(self):
        """Displays video currently playing."""

        if self._current_video == 'none':
            print('No video is currently playing')
        elif self._current_video != 'none':
            if self._current_video == self._paused_video:
                print(f'Currently playing: {self._video_library.get_video(self._current_video)._title} ({self._video_library.get_video(self._current_video)._video_id}) {list(self._video_library.get_video(self._current_video)._tags)} - PAUSED')
            else:
                print(f'Currently playing: {self._video_library.get_video(self._current_video)._title} ({self._video_library.get_video(self._current_video)._video_id}) {list(self._video_library.get_video(self._current_video)._tags)}')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlists[playlist_name.lower()] = []
            self._playlist_names.append(playlist_name)
            print(f'Successfully created new playlist: {playlist_name}')

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video_id_list = list(self._video_library._videos.keys())

        if playlist_name.lower() not in self._playlists.keys():
            print(f'Cannot add video to {playlist_name}: Playlist does not exist')
        elif video_id in self._playlists[playlist_name.lower()]:
            print(f'Cannot add video to {playlist_name}: Video already added')
        elif video_id not in video_id_list:
            print(f'Cannot add video to {playlist_name}: Video does not exist')
        else:
            self._playlists[playlist_name.lower()].append(video_id)
            print(f'Added video to {playlist_name}: {self._video_library.get_video(video_id)._title}')

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self._playlist_names) == 0:
            print('No playlists exist yet')
        else:
            print('Showing all playlists: ')
            for playlist in self._playlist_names:
                print(playlist)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists.keys():
            print(f'Cannot show playlist {playlist_name}: Playlist does not exist')
        else:
            if self._playlists.get(playlist_name.lower()) == []:
                print(f'Showing playlist: {playlist_name}')
                print('No videos here yet')
            else:
                print(f'Showing playlist: {playlist_name}')
                for item in self._playlists.get(playlist_name.lower()):
                    print(f'{self._video_library.get_video(item)._title} ({self._video_library.get_video(item)._video_id}) {list(self._video_library.get_video(item)._tags)}')


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        video_id_list = list(self._video_library._videos.keys())

        if playlist_name.lower() not in self._playlists.keys():
            print(f'Cannot remove video from {playlist_name}: Playlist does not exist')
        elif video_id not in video_id_list:
            print(f'Cannot remove video from {playlist_name}: Video does not exist')
        elif video_id not in self._playlists.get(playlist_name.lower()):
            print(f'Cannot remove video from {playlist_name}: Video is not in playlist')
        else:
            self._playlists[playlist_name.lower()].remove(video_id)
            print(f'Removed video from {playlist_name}: {self._video_library.get_video(video_id)._title}')


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists.keys():
            print(f'Cannot clear playlist {playlist_name}: Playlist does not exist')
        else:
            self._playlists[playlist_name.lower()].clear()
            print(f'Successfully removed all videos from {playlist_name}')


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists.keys():
            print(f'Cannot delete playlist {playlist_name}: Playlist does not exist')
        else:
            self._playlists.pop(playlist_name.lower())
            print(self._playlists)
            print(f'Deleted playlist: {playlist_name}')

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        videos = {}
        for item in self._video_library.get_all_videos():
            videos[item._video_id] = item._title

        match = []
        for video in videos:
            title = videos.get(video)
            if search_term.lower() in title.lower():
                match.append(video)

        # print statements
        if len(match) == 0:
            print(f'No search results for {search_term}')
        else:
            print(f"Here are the results for {search_term}: ")
            number_range = range(1, len(match)+1)
            for i in number_range:
                print(f'{i}) {self._video_library.get_video(match[i-1])._title} ({self._video_library.get_video(match[i-1])._video_id}) {list(self._video_library.get_video(match[i-1])._tags)}')
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print("If your answer is not a valid number, we will assume it's a no.")

            video_choice = input("")

            if int(video_choice) in number_range:
                video_choice_id = match[int(video_choice)-1]
                self.play_video(video_choice_id)



    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = {}
        for item in self._video_library.get_all_videos():
            videos[item._video_id] = item._tags


        match = []
        for video in videos:
            tags = videos.get(video)
            if video_tag.lower() in tags:
                match.append(video)

        # print statements
        if len(match) == 0:
            print(f'No search results for {video_tag}')
        else:
            print(f"Here are the results for {video_tag}: ")
            number_range = range(1, len(match) + 1)
            for i in number_range:
                print(
                    f'{i}) {self._video_library.get_video(match[i - 1])._title} ({self._video_library.get_video(match[i - 1])._video_id}) {list(self._video_library.get_video(match[i - 1])._tags)}')
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print("If your answer is not a valid number, we will assume it's a no.")

            video_choice = input("")

            if int(video_choice) in number_range:
                video_choice_id = match[int(video_choice) - 1]
                self.play_video(video_choice_id)



    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
