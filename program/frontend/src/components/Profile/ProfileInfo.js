import React, { useEffect, useState } from 'react';
import { getProfile, updateProfile } from '../../services/api';

const ProfileInfo = () => {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const profileData = await getProfile();
        setProfile(profileData);
      } catch (error) {
        console.error('Error fetching profile:', error);
      }
    };

    fetchProfile();
  }, []);

  const handleUpdateProfile = async () => {
    try {
      // Replace 'newUsername' and 'newemail@example.com' with the actual values
      const updatedProfile = await updateProfile('newUsername', 'newemail@example.com');
      console.log('Profile updated:', updatedProfile);
      // Update the profile state with the new data, if needed
    } catch (error) {
      console.error('Error updating profile:', error);
    }
  };

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div>
        <p>Username: {profile.username}</p>
        <p>Email: {profile.email}</p>
      </div>
      {/* Add a button or form to trigger the handleUpdateProfile function */}
      <button onClick={handleUpdateProfile}>Update Profile</button>
    </div>
  );
};

export default ProfileInfo;