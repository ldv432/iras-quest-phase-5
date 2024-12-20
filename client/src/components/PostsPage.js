import React, { useState, useEffect } from "react";
import {
  Box,
  Card,
  CardContent,
  IconButton,
  Typography,
  TextField,
  Button,
} from "@mui/material";
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
import Navbar from "./Navbar";

function PostsPage({ currentUser }) {
  const [posts, setPosts] = useState([]); // Posts
  const [userReactions, setUserReactions] = useState({});
  const [newPost, setNewPost] = useState("");

  // Fetch posts and user reactions
  useEffect(() => {
    // if (!currentUser) return;

    // Fetch Posts
    fetch("/forum/posts")
      .then((res) => res.json())
      .then((data) => setPosts(data))
      .catch((error) => console.error("Error fetching posts:", error));

    // Fetch User Reactions
    fetch("/forum/reactions", { credentials: "include" })
      .then((res) => res.json())
      .then((data) => {
        console.log(Object.keys(data))
        const reactions = {};
        Object.keys(data).forEach(postId => {
        let reactionData = data[postId]["counts"]
        reactionData["user"] = data[postId]["user"]
        console.log(reactionData)
        reactions[postId] = reactionData
        })
        // data.forEach(({ post_id, reaction_type, count, user_reacted }) => {
        //   if (!reactions[post_id]) {
        //     reactions[post_id] = { like: 0, dislike: 0, favorite: 0, user: {} };
        //   }
        //   reactions[post_id][reaction_type] = count;
        //   reactions[post_id].user[reaction_type] = user_reacted;
        // });
        console.log(reactions)
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
        setPosts((prevPosts) => [data, ...prevPosts]); // Add new post to state
        setNewPost(""); // Clear input field
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
        reaction_id: reactionId, // Ensure this is a number
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
          console.log(userReactions)

          // Update counts and toggle based on backend response
          const updatedReactions = {
            ...postReactions,
            [reactionId]: data.count, // Update count from backend
            user: {
              ...postReactions.user,
              [reactionId]: data.status === "added", // Toggle user reaction
            },
          };

          return { ...prev, [postId]: updatedReactions };
        });
      })
      .catch((error) => console.error("Error toggling reaction:", error));
  };

  return (
    <>
      <Navbar />
      <Box sx={{ p: 3 }}>
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
            boxShadow: "0 2px 5px rgba(0,0,0,0.2)",
            borderRadius: "8px",
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
                {/* Username on the left */}
                <Typography variant="h6" sx={{ fontWeight: "bold" }}>
                  {post.user?.username || "Unknown User"}
                </Typography>

                {/* Date and Time on the right */}
                <Typography
                  variant="caption"
                  color="textSecondary"
                  sx={{ textAlign: "right" }}
                >
                  {new Date(post.created_at).toLocaleString(undefined, {
                    year: "numeric",
                    month: "short",
                    day: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                    hour12: true,
                  })}
                </Typography>
              </Box>

              {/* Post Content */}
              <Typography variant="body1" sx={{ mb: 1 }}>
                {post.content}
              </Typography>
              {/* Reaction Buttons */}
              <Box sx={{ display: "flex", gap: 2, mt: 2 }}>
                {/* Like Button */}
                <IconButton
                  onClick={() => toggleReaction(post.id, 1)} // Pass as number (no quotes)
                  color={
                    userReactions[post.id]?.user[1] ? "primary" : "default"
                  }
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

                {/* Dislike Button */}
                <IconButton
                  onClick={() => toggleReaction(post.id, 2)} // Pass as number
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

                {/* Favorite Button */}
                <IconButton
                  onClick={() => toggleReaction(post.id, 3)} // Pass as number
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
              </Box>

              {/* Edit/Delete Buttons */}
              {post.user_id === currentUser?.id && (
                <Box
                  sx={{ display: "flex", gap: 1, alignItems: "center", mt: 1 }}
                >
                  <IconButton
                    onClick={() => {
                      const updatedContent = prompt(
                        "Edit your post:",
                        post.content
                      );
                      if (updatedContent) {
                        console.log("Edit post:", updatedContent);
                      }
                    }}
                    color="info"
                  >
                    <Edit />
                  </IconButton>
                  <IconButton
                    onClick={() => console.log("Delete post:", post.id)}
                    color="error"
                  >
                    <Delete />
                  </IconButton>
                </Box>
              )}
            </CardContent>
          </Card>
        ))}
      </Box>
    </>
  );
}

export default PostsPage;
