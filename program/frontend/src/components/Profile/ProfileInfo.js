import React, { useState, useEffect } from 'react';
import { Box, Typography, Button } from '@mui/material';
import { getProfile, updateProfile } from '../../services/api';
import { TextField } from '@mui/material';

const ProfileInfo = () => {
  const [profile, setProfile] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const profileData = await getProfile();
        setProfile(profileData);
        setUsername(profileData.username);
        setEmail(profileData.email);
      } catch (error) {
        console.error('Error fetching profile:', error);
      }
    };

    fetchProfile();
  }, []);

  const handleUpdateProfile = async () => {
    try {
      const updatedProfile = await updateProfile(username, email);
      setProfile(updatedProfile);
      setEditMode(false);
    } catch (error) {
      console.error('Error updating profile:', error);
    }
  };

  const handleEditProfile = () => {
    setEditMode(true);
  };

  const handleCancelEdit = () => {
    setEditMode(false);
    setUsername(profile.username);
    setEmail(profile.email);
  };

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        maxWidth: 600,
        mx: 'auto',
        my: 4,
        p: 4,
        bgcolor: 'background.paper',
        borderRadius: 2,
        boxShadow: 2,
      }}
    >
      <Typography variant="h5" component="h1" gutterBottom>
        Profile Information
      </Typography>
      {editMode ? (
        <Box sx={{ display: 'flex', flexDirection: 'column', width: '100%' }}>
          <TextField
            label="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            margin="normal"
          />
          <TextField
            label="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            margin="normal"
          />
          <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 2 }}>
            <Button
              variant="contained"
              color="primary"
              onClick={handleUpdateProfile}
            >
              Save
            </Button>
            <Button variant="outlined" onClick={handleCancelEdit}>
              Cancel
            </Button>
          </Box>
        </Box>
      ) : (
        <Box>
          <Typography variant="body1">Username: {profile.username}</Typography>
          <Typography variant="body1">Email: {profile.email}</Typography>
          <Button
            variant="contained"
            color="primary"
            onClick={handleEditProfile}
            sx={{ mt: 2 }}
          >
            Edit Profile
          </Button>
        </Box>
      )}
    </Box>
  );
};

export default ProfileInfo;