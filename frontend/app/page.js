// import Image from "next/image";
// import styles from "./page.module.css";
"use client"
import React, { useEffect, useState } from "react";

export default function Home() {

  useEffect(() => {
    fetch("http://127.0.0.1:8080/?").then(
      response => response.json()
    ).then((data) => {
      console.log(data);
    });
  }, []);

  return (
    <main>
      <p>Hello, World!</p>
    </main>
  );
}
