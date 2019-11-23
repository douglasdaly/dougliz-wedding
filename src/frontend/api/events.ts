// api/events.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IEventsAPI } from './types'

const EventsAPI = function (axios: NuxtAxiosInstance): IEventsAPI {
  return {
    async createEvent (event) {
      const res = await axios.post('/events', event);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getUpcomingEvents (skip, limit) {
      const res = await axios.get('/events', { params: { skip, limit } });
      if (res.status === 200) {
        return res.data;
      }
    },

    async getAllEvents (skip, limit) {
      const res = await axios.get('/events/all', { params: { skip, limit } });
      if (res.status === 200) {
        return res.data;
      }
    },

    async getEvent (eventId) {
      const res = await axios.get(`/events/${eventId}`);
      if (res.status === 200) {
        return res.data;
      }
    },

    async updateEvent (eventId, data) {
      const res = await axios.put(`/events/${eventId}`, data);
      if (res.status === 200) {
        return res.data;
      }
    },

    async deleteEvent (eventId) {
      const res = await axios.delete(`/events/${eventId}`);
      if (res.status === 200) {
        return res.data;
      }
    }
  }
};

export default EventsAPI;
