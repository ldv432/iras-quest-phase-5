const GamePage = () => {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "calc(100vh - 60px)", // Adjust this based on your navbar height
        marginTop: "60px", // Space for the navbar
      }}
    >
      <iframe
        src="https://ldv432.github.io/iras-quest-game/"
        title="Pygbag Game"
        width="1400px" // Set the desired width
        height="1000px" // Set the desired height
        style={{ border: "none" }}
      ></iframe>
    </div>
  );
};

export default GamePage;
