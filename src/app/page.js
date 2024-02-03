'use client'
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';
import styles from "./page.module.css";
import "react-big-calendar/lib/css/react-big-calendar.css";
import {useState} from "react";


const localizer = momentLocalizer(moment)

export default function Home() {
  return (
    <main className={styles.main}>
      <div>
        <p>
          Health AI running plan
        </p>
          <Calendar
              localizer={localizer}
              startAccessor="start"
              endAccessor="end"
              style={{ height: 500 }}
          />
      </div>
    </main>
  );
}
