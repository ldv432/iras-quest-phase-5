import React, { useState, useEffect, useContext } from "react";
import { UserContext } from "./UserContext";
import {
  Box,
  Card,
  CardContent,
  IconButton,
  Typography,
  TextField,
  Button,
  Modal,
} from "@mui/material";
import castleImage from "../assets/pictures/Splash.png";
import {
  Favorite,
  FavoriteBorder,
  ThumbUp,
  ThumbUpOffAlt,
  ThumbDown,
  ThumbDownOffAlt,
  Edit,
  Delete,
} from "@mui/icons-material";

const PostsPage = () => {
  const [posts, setPosts] = useState([]);
  const [userReactions, setUserReactions] = useState({});
  const [newPost, setNewPost] = useState("");
  const [editModalOpen, setEditModalOpen] = useState(false);
  const [editPost, setEditPost] = useState(null);
  const [editContent, setEditContent] = useState("");
  const { currentUser } = useContext(UserContext);

  // Fetch posts and user reactions
  useEffect(() => {
    fetch("/forum/posts")
      .then((res) => res.json())
      .then((data) => setPosts(data))
      .catch((error) => console.error("Error fetching posts:", error));

    fetch("/forum/reactions", { credentials: "include" })
      .then((res) => res.json())
      .then((data) => {
        const reactions = {};
        Object.keys(data).forEach((postId) => {
          let reactionData = data[postId]["counts"];
          reactionData["user"] = data[postId]["user"];
          reactions[postId] = reactionData;
        });
        setUserReactions(reactions);
      })
      .catch((error) => console.error("Error fetching reactions:", error));
  }, [currentUser]);

  const handlePostSubmit = (e) => {
    e.preventDefault();
    fetch("/forum/posts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ content: newPost }),
    })
      .then((res) => res.json())
      .then((data) => {
        setPosts((prevPosts) => [data, ...prevPosts]);
        setNewPost("");
      })
      .catch((error) => console.error("Error adding post:", error));
  };

  const toggleReaction = (postId, reactionId) => {
    fetch(`/post-reactions`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({
        post_id: postId,
        reaction_id: reactionId,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setUserReactions((prev) => {
          const postReactions = prev[postId] || {
            1: 0,
            2: 0,
            3: 0,
            user: {},
          };
          const updatedReactions = {
            ...postReactions,
            [reactionId]: data.count,
            user: {
              ...postReactions.user,
              [reactionId]: data.status === "added",
            },
          };
          return { ...prev, [postId]: updatedReactions };
        });
      })
      .catch((error) => console.error("Error toggling reaction:", error));
  };

  const handleEditClick = (post) => {
    setEditPost(post);
    setEditContent(post.content);
    setEditModalOpen(true);
  };

  const handleEditSubmit = () => {
    fetch(`/forum/posts/${editPost.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ content: editContent }),
    })
      .then((res) => res.json())
      .then((updatedPost) => {
        setPosts((prevPosts) =>
          prevPosts.map((post) =>
            post.id === updatedPost.id ? updatedPost : post
          )
        );
        setEditModalOpen(false);
        setEditPost(null);
        setEditContent("");
      })
      .catch((error) => console.error("Error editing post:", error));
  };

  const handleDelete = (postId) => {
    fetch(`/forum/posts/${postId}`, {
      method: "DELETE",
      credentials: "include",
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to delete post");
        setPosts((prevPosts) => prevPosts.filter((post) => post.id !== postId));
      })
      .catch((error) => console.error("Error deleting post:", error));
  };

  const handleModalClose = () => {
    setEditModalOpen(false);
    setEditPost(null);
    setEditContent("");
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "100vh",
        bgcolor: "#f5f5f5",
        gap: 4,
        px: 4,
      }}
    >
      {/* Image Section */}
      <Box>
        <img
          src={castleImage}
          alt="Ira's Quest Castle"
          style={{
            width: "500px",
            height: "500px",
            objectFit: "cover",
          }}
        />
      </Box>

      {/* Content Section */}
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          gap: 2,
          width: "600px",
          p: 3,
          borderRadius: "8px",
          boxShadow: "0 4px 10px rgba(0, 0, 0, 0.2)",
          bgcolor: "white",
        }}
      >
        {/* Post Form */}
        <Box
          component="form"
          onSubmit={handlePostSubmit}
          sx={{
            display: "flex",
            flexDirection: "column",
            gap: 2,
            mb: 4,
            p: 2,
            borderRadius: "8px",
            boxShadow: "0 2px 5px rgba(0,0,0,0.2)",
            bgcolor: "white",
          }}
        >
          <Typography variant="h6">Create a New Post</Typography>
          <TextField
            multiline
            rows={3}
            variant="outlined"
            placeholder="What's on your mind?"
            value={newPost}
            onChange={(e) => setNewPost(e.target.value)}
            required
          />
          <Button
            type="submit"
            variant="contained"
            color="primary"
            disabled={!newPost.trim()}
          >
            Post
          </Button>
        </Box>

        {/* Posts List */}
        {posts.map((post) => (
          <Card
            key={post.id}
            sx={{
              mb: 2,
              p: 2,
              boxShadow: "none",
              border: "1px solid #ddd",
            }}
          >
            <CardContent>
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  mb: 1,
                }}
              >
                <Typography variant="h6" sx={{ fontWeight: "bold" }}>
                  {post.user?.username || "Unknown User"}
                </Typography>
                <Typography
                  variant="caption"
                  color="textSecondary"
                  sx={{ textAlign: "right" }}
                >
                  {new Date(post.created_at).toLocaleString()}
                </Typography>
              </Box>
              <Typography variant="body1" sx={{ mb: 1 }}>
                {post.content}
              </Typography>
              <Box sx={{ display: "flex", gap: 2, mt: 2 }}>
                {/* Reactions */}
                <IconButton
                  onClick={() => toggleReaction(post.id, 1)}
                  color={userReactions[post.id]?.user[1] ? "primary" : "default"}
                >
                  {userReactions[post.id]?.user[1] ? (
                    <ThumbUp />
                  ) : (
                    <ThumbUpOffAlt />
                  )}
                  <Typography variant="caption" sx={{ ml: 0.5 }}>
                    {userReactions[post.id]?.[1] || 0}
                  </Typography>
                </IconButton>
                <IconButton
                  onClick={() => toggleReaction(post.id, 2)}
                  color={userReactions[post.id]?.user[2] ? "error" : "default"}
                >
                  {userReactions[post.id]?.user[2] ? (
                    <ThumbDown />
                  ) : (
                    <ThumbDownOffAlt />
                  )}
                  <Typography variant="caption" sx={{ ml: 0.5 }}>
                    {userReactions[post.id]?.[2] || 0}
                  </Typography>
                </IconButton>
                <IconButton
                  onClick={() => toggleReaction(post.id, 3)}
                  color={
                    userReactions[post.id]?.user[3] ? "secondary" : "default"
                  }
                >
                  {userReactions[post.id]?.user[3] ? (
                    <Favorite />
                  ) : (
                    <FavoriteBorder />
                  )}
                  <Typography variant="caption" sx={{ ml: 0.5 }}>
                    {userReactions[post.id]?.[3] || 0}
                  </Typography>
                </IconButton>
                {/* Edit and Delete Buttons */}
                {post.user_id === currentUser?.id && (
                  <>
                    <IconButton
                      onClick={() => handleEditClick(post)}
                      color="info"
                    >
                      <Edit />
                    </IconButton>
                    <IconButton
                      onClick={() => handleDelete(post.id)}
                      color="error"
                    >
                      <Delete />
                    </IconButton>
                  </>
                )}
              </Box>
            </CardContent>
          </Card>
        ))}
      </Box>

      {/* Edit Post Modal */}
      <Modal
        open={editModalOpen}
        onClose={handleModalClose}
        aria-labelledby="edit-post-modal"
        aria-describedby="edit-post-modal-description"
      >
        <Box
          sx={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: 400,
            bgcolor: "white",
            p: 4,
            borderRadius: "8px",
            boxShadow: 24,
          }}
        >
          <Typography id="edit-post-modal" variant="h6" sx={{ mb: 2 }}>
            Edit Post
          </Typography>
          <TextField
            multiline
            rows={4}
            fullWidth
            variant="outlined"
            value={editContent}
            onChange={(e) => setEditContent(e.target.value)}
            sx={{ mb: 2 }}
          />
          <Button
            variant="contained"
            color="primary"
            onClick={handleEditSubmit}
            fullWidth
          >
            Save Changes
          </Button>
        </Box>
      </Modal>
    </Box>
  );
};

export default PostsPage;
