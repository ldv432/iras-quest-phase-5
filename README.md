# Ira's Quest: Full-Stack RPG side-scroller game, soon-to-be platformer
**Welcome to Ira's Quest!** This project is a labor of love, combining a React frontend, a Flask backend, and a Pygame-based game, all dedicated to my son, Ira. The application integrates dynamic gameplay, a social forum, and user account management to create a multifaceted web experience.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Code Highlights](#code-highlights)
- [Setup and Installation](#setup-and-installation)
- [Game Design](#game-design)
- [Acknowledgments](#acknowledgments)

---

## Project Overview
Ira's Quest is a full-stack web application featuring:
- A **Pygame-powered platformer game** embedded seamlessly within a React app.
- A **React frontend** styled with MUI (Material-UI) for a modern, responsive design.
- A **Flask API backend** utilizing SQLAlchemy for database interactions, ensuring a secure and efficient user experience.

The game, "Ira's Quest," was designed to combine fun gameplay with opportunities for users to engage socially through forum posts and reactions.

---

## Tech Stack
### Frontend
- **React** with React Router for navigation.
- **Material-UI (MUI)** for sleek and responsive styling.

### Backend
- **Flask** API for managing user authentication and interactions.
- **SQLAlchemy** ORM for database models and relationships.

### Game Engine
- **Pygame** for immersive 2D gameplay.
- Deployed to "Github Pages" via **WebAssembly** using Pygbag for web compatibility. 
---

## Features
### Gameplay
- Pygame-based platformer with dynamic obstacles and animations.
- Fully playable through an iframe integration in React.

### User System
- Account creation and login with secure password storage using Flask-Bcrypt.
- Context API for managing user state across React components.

### Forum
- Users can create posts, edit, delete, and react to others' content.
- Integrated reaction system with likes, dislikes, and favorites.

### Responsive Design
- Material-UI styling ensures compatibility with various screen sizes.
- Flexbox layout adjustments for seamless embedding and alignment.

---

## Code Highlights
### Seamless Pygame Integration
The Pygame game is hosted on GitHub Pages and embedded into React using the following component:

```jsx
const GamePage = () => {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "calc(100vh - 60px)",
        marginTop: "60px",
      }}
    >
      <iframe
        src="https://ldv432.github.io/iras-quest-game/"
        title="Pygbag Game"
        width="1400px"
        height="1000px"
        style={{ border: "none" }}
      ></iframe>
    </div>
  );
};
```

### Forum Reaction System
Efficient management of user reactions to posts:

```python
class AddReaction(Resource):
    def post(self):
        if "user_id" not in session:
            return {"error": "You must login to react to this post"}, 400

        data = request.json
        reaction_id = data.get('reaction_id')
        post_id = data.get('post_id')

        # Toggle reaction logic
        existing_reaction = PostReaction.query.filter_by(
            user_id=session['user_id'], post_id=post_id, reaction_id=reaction_id
        ).first()

        if existing_reaction:
            db.session.delete(existing_reaction)
        else:
            new_reaction = PostReaction(user_id=session['user_id'], post_id=post_id, reaction_id=reaction_id)
            db.session.add(new_reaction)

        db.session.commit()
        return {"message": "Reaction toggled successfully"}, 200
```

---

## Setup and Installation
### Prerequisites
- Node.js and npm
- Python 3.9+
- SQLite (or your preferred database)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ldv432/iras-quest
   cd iras-quest
   ```

2. Install frontend dependencies:
   ```bash
   cd client/   
   npm install
   ```

3. Install backend dependencies:
   ```bash
   cd server/
   pip install
   ```


### Run the Application
- Start the Flask backend:
  ```bash
  flask run
  ```

- Start the React frontend:
  ```bash
  cd client/
  npm start
  ```

Access the application at `http://localhost:3000`.

---

## Game Design
Special thanks to:
- ClearCode's pygame youtube tutorial, his videos assisted in both versions of the game that I created (https://www.youtube.com/watch?v=AY9MnQ4x3zk)
- RottingPixel's Dungeon Assets on OpenGameArt (https://opengameart.org/content/2d-dungeon-platformer-tileset-16x16)
- Buch's Character and Monster Assets on OpenGameArt (https://opengameart.org/content/a-platformer-in-the-forest)
- SUNO AI Generated Music (https://suno.com/song/9f9253eb-2425-4317-a7f9-139572a24b7f)

---

## Acknowledgments
This project would not have been possible without:
- The **Pygame community** for inspiring game development.
- **GitHub Pages** for enabling easy hosting of the game.
- **Material-UI** for making responsive design a breeze.
- My son, Ira, whose name and spirit brought this project to life. 

I hope you enjoy Ira's Quest as much as I enjoyed creating it!