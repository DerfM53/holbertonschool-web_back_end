export default async function loadBalancer(chinaDownload, USDownload) {
  try {
    const result = await Promise.race([chinaDownload, USDownload]);
    return result;
  } catch (error) {
    throw error;
  }
}
