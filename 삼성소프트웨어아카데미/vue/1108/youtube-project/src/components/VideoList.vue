<template>
  <ul>
    <video-list-item
      v-for="(video, idx) in videos"
      :key="idx"
      :video="video"
      @select-video="onSelectVideo"
    >
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required:true,
    }
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>
