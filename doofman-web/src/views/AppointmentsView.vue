<script lang="ts">
import { defineComponent } from 'vue'

interface Appointment {
  date: {
    $date: Date
  },
  notes: string,
  patient_id: string,
  status: number
}

export default defineComponent({
    props: {},
    data() {
      return {
        appointments: []
      }
    },
    methods: {
      async getAppointments() {
        let param: string = 'all';
        if (this.$route.params.id !== undefined) {
          param = this.$route.params.id as string;
        } else {
          param = 'all';
        }
        this.appointments = await (await fetch("http://127.0.0.1:8000/appointment/" + param)).json();     
      },
      getDate(obj: Appointment): Date {
        return obj.date.$date
      }
    },
    mounted() {
      
    },
    created() {
      this.getAppointments();
    },
    computed: {

    }

})

</script>

<template>
  <main>
    <ul>
      <li v-for="appointment in appointments">
        {{ getDate(appointment) }}     
      </li>
    </ul>
    <p v-if="appointments?.length == 0">No appointments found!</p>
  </main>
</template>
