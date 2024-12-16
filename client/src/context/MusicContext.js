// src/context/MusicContext.js
import React, { createContext, useRef, useEffect } from 'react';

// Create Context
export const MusicContext = createContext();

// Music Provider Component
export function MusicProvider({ children }) {
  const audioRef = useRef(null);

  useEffect(() => {
    // Automatically play music when the app loads
    if (audioRef.current) {
      audioRef.current.play().catch((err) => {
        console.log("Music autoplay blocked by browser. Will play after user interaction.");
      });
    }
  }, []);

  const playMusic = () => {
    audioRef.current?.play();
  };

  const pauseMusic = () => {
    audioRef.current?.pause();
  };

  return (
    <MusicContext.Provider value={{ playMusic, pauseMusic }}>
      {children}
      <audio ref={audioRef} loop>
        <source src="/assets/music/IrasQuest.ogg" type="audio/mpeg" />
        Your browser does not support the audio element.
      </audio>
    </MusicContext.Provider>
  );
}
